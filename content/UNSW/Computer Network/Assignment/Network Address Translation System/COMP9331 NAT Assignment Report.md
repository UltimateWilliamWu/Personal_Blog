---
aliases:
  - COMP3331/COMP9331 NAT Assignment Report
---
## 1. Code Organisation

The implementation is organised around a small command-line entry point and a set of protocol/runtime modules.

- `nat.py`
  Parses the six required command-line arguments, validates them, constructs a `NATConfig`, and starts the runtime.
- `nat_system/runtime.py`
  Contains the main NAT event loop and the end-to-end forwarding logic. It creates the real UDP sockets, listens on both interfaces, validates incoming packets, performs translation, handles TTL and ICMP generation, and applies fragmentation or reassembly when needed.
- `nat_system/packets.py`
  Defines the logical packet abstractions used by the assignment model:
  - `IPv4Packet`
  - `UDPSegment`
  - `ICMPMessage`
  
  This module is responsible for parsing raw bytes, serialising headers back to bytes, and generating/verifying checksums.
- `nat_system/translation.py`
  Implements the NAT translation table and external-port allocation logic.
- `nat_system/reassembly.py`
  Implements buffering and reassembly for fragmented IPv4 datagrams.
- `nat_system/util.py`
  Provides constants, IPv4 parsing/formatting helpers, and the Internet checksum function.

The main program flow is:

1. `nat.py` validates `external_ip`, `num_external_ports`, `timeout`, `mtu`, `real_internal_port`, and `real_next_hop_port`.
2. `NATRuntime` binds:
   - an internal UDP socket to `real_internal_port`
   - an external UDP socket to port `0`, allowing the OS to allocate an ephemeral port
3. Both sockets are registered with `selectors.DefaultSelector` and processed in a single event-driven loop.
4. On packet arrival, the runtime:
   - determines direction from the receiving socket
   - parses the logical IPv4 packet
   - validates the IP checksum
   - reassembles fragments if necessary
   - dispatches to UDP or ICMP handlers
5. For outbound UDP traffic, the NAT allocates or reuses a mapping, rewrites source IP and source port, decrements TTL, recomputes checksums, and fragments the datagram if it exceeds the configured MTU.
6. For inbound UDP replies, the NAT finds the reverse mapping, restores the original internal destination IP and port, decrements TTL, recomputes checksums, and sends the packet back to the client-side real UDP endpoint.
7. For relevant ICMP error traffic arriving from the external side, the NAT rewrites the quoted inner IPv4/UDP header so the internal sender can identify the original flow.

## 2. Data Structures

### 2.1 Translation Table

The translation state is represented by `NatMapping` objects:

- `internal_ip`
- `internal_port`
- `external_port`
- `last_used`

`TranslationTable` keeps two dictionaries:

- `_by_internal[(internal_ip, internal_port)] -> NatMapping`
- `_by_external[external_port] -> NatMapping`

This gives efficient lookup in both directions:

- outbound traffic indexes by internal flow and either reuses or allocates an external port
- inbound traffic indexes by translated external port and recovers the original internal destination

A `deque` stores currently available external ports from `1` to `num_external_ports`. When an idle mapping expires, its port is returned to this pool.

### 2.2 Fragment Reassembly State

Inbound fragments are tracked in `ReassemblyTable`, keyed by:

- `(interface_name, identification)`

This matches the assignment assumption that fragment identification values are globally unique, so more complex keys are unnecessary in this model.

Each `FragmentGroup` stores:

- `first_header`
- `expected_length`
- `last_update`
- `fragments[offset] -> payload_bytes`

When all fragment ranges become contiguous from offset `0` to the final length, the NAT reconstructs a complete logical IPv4 datagram and passes it back into normal packet handling.

### 2.3 Protocol Objects

The packet module uses explicit structured objects instead of manipulating raw byte arrays everywhere:

- `IPv4Packet` stores header fields such as source and destination address, identification, flags, fragment offset, TTL, protocol, and payload
- `UDPSegment` stores ports, payload, length, and checksum
- `ICMPMessage` stores type, code, rest-of-header, payload data, and checksum

This design keeps the NAT logic readable while still preserving byte-accurate serialisation for forwarding.

## 3. Concurrency Handling

The NAT is implemented as a single-threaded event-driven system using non-blocking sockets and `selectors.DefaultSelector`.

This design was chosen for two reasons:

1. The assignment requires the NAT to listen on both internal and external sockets without assuming a strict request-response pattern.
2. A selector-based design avoids lock management and shared-state races that would arise with a multi-threaded implementation.

At runtime, both sockets are registered with the selector. Each iteration of the main loop:

- expires stale NAT mappings and fragment reassembly state
- waits for readability events on either socket
- drains each ready socket until it would block

This means the NAT can process:

- multiple outbound flows
- inbound replies arriving at arbitrary times
- reassembly and timeout maintenance

without blocking on one interface while packets are waiting on the other.

## 4. Known Limitations and Assumptions

This section reflects the current implementation rather than an idealised design.

- The implementation follows the assignment model only. It assumes fixed 20-byte IPv4 headers with no options, UDP application traffic, and ICMP error messages relevant to the assignment.
- Real transport is restricted to localhost UDP sockets. The runtime accepts inbound external traffic only from the configured `real_next_hop_port`, which is consistent with the specification.
- The logical internal network is represented by a single real UDP client endpoint. The runtime sends all internal replies to the most recently observed internal sender address, which matches the provided single-client model.
- Generated ICMP error packets use the configured `external_ip` as the logical source address. The specification does not define a separate logical internal NAT interface address, so this implementation keeps one NAT-visible logical address.
- Fragment reassembly uses `(interface, identification)` as the reassembly key and therefore relies on the specification’s assumption that identification values are globally unique.
- The implementation is intentionally correctness-oriented rather than throughput-oriented. It is suitable for the assignment scale, but it does not attempt advanced optimisation of buffer growth, batching, or high-volume logging.

## 5. Discussion

### 5.1 NAT and the Layering Principle

NAT weakens the strict layering principle because it cannot operate purely at the IP layer. A router that performs only normal IPv4 forwarding can route packets using source and destination addresses alone. In contrast, this NAT must inspect and rewrite UDP source and destination ports in order to multiplex flows onto a limited external port space.

This creates cross-layer dependence:

- the network-layer device must parse transport-layer headers
- UDP checksums must be recomputed after address or port translation because the checksum includes an IPv4 pseudo-header
- ICMP error handling also depends on understanding the quoted inner IPv4 and UDP headers

As a result, NAT is best viewed as a practical middlebox mechanism rather than a cleanly layered network-layer function.

### 5.2 NAT and the End-to-End Principle

NAT also weakens the end-to-end principle. In an ideal end-to-end design, communication semantics are determined primarily by the endpoints, while the network simply forwards packets. NAT introduces per-flow state in the middle of the path:

- new outbound traffic creates translation state inside the NAT
- unsolicited inbound traffic is dropped when no state exists
- ongoing communication depends on timeout behaviour and mapping lifetime inside the middlebox

This means reachability and correctness are no longer determined only by sender and receiver. The middlebox becomes part of the communication semantics, especially for timeouts, ICMP handling, fragmentation, and reverse-path delivery.

### 5.3 Advantages of NAT

1. **Address hiding and basic exposure reduction**
   
   Internal hosts and their private addresses are not directly visible to the external network. In this assignment model, unmatched inbound packets are silently dropped, which reduces accidental exposure of internal services.

2. **Easier internal network renumbering**
   
   Internal hosts can continue using the same private address space even if the externally visible address changes. This decouples internal addressing from provider-facing addressing and simplifies local network administration.

3. **Centralised policy point**
   
   Because the NAT already inspects, filters, and rewrites traffic, it naturally becomes a control point for timeout rules, inbound filtering, and ICMP generation.

### 5.4 Disadvantages of NAT

1. **Breaks direct end-to-end reachability**
   
   External hosts cannot normally initiate communication with internal hosts unless suitable translation state already exists. This makes peer-to-peer communication and inbound service hosting more complicated.

2. **Adds protocol complexity**
   
   The NAT must maintain state, rewrite headers, recompute checksums, handle fragmentation and reassembly, and translate certain ICMP errors. This is significantly more complex than ordinary stateless forwarding.

3. **Creates dependence on middlebox behaviour**
   
   Communication can fail because of timeout expiry, port exhaustion, or inconsistent NAT behaviour rather than endpoint logic alone. This increases operational complexity and makes debugging harder.

## 6. References

1. UNSW School of Computer Science and Engineering. *COMP3331/9331 26T1 Assignment Specification: Building a Network Address Translation System*. Term 1, 2026.
2. UNSW School of Computer Science and Engineering. *COMP3331/9331 26T1 Assignment Testing: Testing Your Network Address Translation System*. Term 1, 2026.
3. Postel, J. *RFC 791: Internet Protocol*. Internet Engineering Task Force, 1981.
4. Postel, J. *RFC 768: User Datagram Protocol*. Internet Engineering Task Force, 1980.
5. Postel, J. *RFC 792: Internet Control Message Protocol*. Internet Engineering Task Force, 1981.
