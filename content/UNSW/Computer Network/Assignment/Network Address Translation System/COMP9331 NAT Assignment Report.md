## 1. Code Organisation

The code structure is:

```text
Network Address Translation System/
|-- nat.py
|-- nat_system/
    |-- __init__.py
    |-- runtime.py
    |-- packets.py
    |-- translation.py
    |-- reassembly.py
    |-- util.py
```

The figure below shows how the main parts of the NAT process work together.

<div align="center">
  <img src="Pasted%20image%2020260406181708.png" width="1500">
  <div><em>Figure 1. Overall NAT process structure.</em></div>
</div>

**nat.py** is the entry point. Its purpose is to handle startup. It takes the six command-line arguments, validates them, builds a **NATConfig** object, and then starts the runtime. In this way, the file turns raw user input into a clean configuration for the rest of the program, or stops early with a clear error if the arguments are invalid.

**nat_system/__init__.py** only defines the package. It does not process packets, but it keeps the project structure clean and makes the main modules easier to import.

**nat_system/runtime.py** contains the main NAT logic. This is the core of the program. It takes the validated configuration and the datagrams arriving on the internal and external UDP sockets. It then creates the sockets, runs the selector loop, checks checksums, decreases TTL, applies NAT translation, handles fragmentation and reassembly, and sends the processed packet to the correct side. The result of this module is the actual forwarding behaviour of the NAT, including translated UDP traffic, generated ICMP errors, fragmented packets, or packet drops when required by the rules.

**nat_system/packets.py** handles packet parsing and packet building. It defines the logical IPv4, UDP, and ICMP packet classes used by the rest of the program. It takes either raw bytes from a socket or structured field values from the runtime, and produces either parsed packet objects or serialised packet bytes. This keeps protocol details out of the runtime and makes the packet-processing code much clearer.

**nat_system/translation.py** manages the NAT mapping table. Its job is to remember which internal flow is using which translated external port. It takes an internal **(IP, port)** pair for outbound traffic or an external port for inbound traffic, together with timing information, and produces a matching mapping, a new mapping, or no mapping when none is available. It also removes idle entries after timeout and returns expired ports to the free pool. This module gives the NAT the state needed to translate traffic consistently across multiple packets.

**nat_system/reassembly.py** manages fragmented IPv4 packets. It takes packet fragments, their interface, and their arrival time, and stores them until a full datagram can be rebuilt. When enough fragments are present, it produces one complete logical IPv4 packet for normal processing. If fragments do not arrive in time, it keeps the state needed for timeout handling. This allows the runtime to work with complete packets instead of incomplete pieces.

**nat_system/util.py** provides shared constants and helper functions. It takes small low-level tasks such as IPv4 parsing, checksum calculation, and protocol definitions, and provides reusable results to the rest of the code. This includes parsed addresses, checksum values, protocol constants, and packet format errors. Keeping these helpers here prevents the main logic files from becoming cluttered.

## 2. Data Structures

The most important data structure is the translation table. Its purpose is to keep NAT state for active UDP flows. Each flow is stored as a **NatMapping** object containing the internal IP, internal port, translated external port, and the time when the mapping was last used. The table keeps two dictionaries over the same mappings. One dictionary supports outbound lookup by **(internal_ip, internal_port)**, and the other supports inbound lookup by **external_port**. A deque stores the currently free external ports. This lets the NAT find mappings quickly in both directions and reuse ports after timeout.

Fragment reassembly uses a separate table because it solves a different problem. A **FragmentGroup** stores the first header, the expected total payload length, the last update time, and a dictionary of fragment payloads keyed by byte offset. The **ReassemblyTable** indexes these groups by **(interface_name, identification)**. As more fragments arrive, the table keeps enough information to decide whether reassembly is complete. Once all byte ranges are present, the fragments are joined into one **IPv4Packet**.

The packet classes are also part of the data design. **IPv4Packet**, **UDPSegment**, and **ICMPMessage** store protocol fields in a structured form instead of leaving them as raw bytes. This gives the runtime a clear representation of the packet it is processing and makes header rewriting, checksum checks, and ICMP generation much easier to manage.

The figure below summarises the two main state structures used by the NAT.

<div align="center">
  <img src="Pasted%20image%2020260406182407.png" width="1500">
  <div><em>Figure 2. Main NAT data structures.</em></div>
</div>

## 3. Concurrency Handling

The NAT uses a single-threaded event-driven design rather than threads. Both UDP sockets are set to non-blocking mode and registered with **selectors.DefaultSelector**. The runtime loop first clears expired NAT mappings and fragment state, then waits for activity on either socket, and processes packets as soon as a socket becomes ready.

The purpose of this design is to let the NAT react to internal and external traffic independently without assuming a fixed request-response order. Internal packets can continue to arrive while external replies are still pending, and external packets can be handled even when no new internal packet has just been seen. Because all shared state is updated in one execution path, the implementation also avoids locks and race conditions.

## 4. Known Limitations

This implementation follows the assignment model rather than a full production NAT. It only supports IPv4 packets with a fixed 20-byte header, UDP traffic, and the ICMP behaviour required by the specification. It does not support IP options or a wider range of transport protocols.

The simplified runtime model also introduces a few practical assumptions. The internal network is represented by one real UDP client endpoint, so replies to the internal side are sent to the most recently seen client address. Generated ICMP error packets use the configured external IP as their source address because the assignment does not define a separate logical internal NAT address. Fragment reassembly also follows the specification assumption that identification values are globally unique, which allows a simpler reassembly key.

## 5. Discussion

NAT weakens the layering principle because it cannot stay inside the IP layer. It must read UDP headers, rewrite UDP port numbers, and recompute the UDP checksum. This means a network device is directly changing transport-layer information.

NAT also weakens the end-to-end principle. Communication now depends on state inside the middlebox. An inbound packet is accepted only if a matching mapping exists. Timeout and port exhaustion inside the NAT can therefore break communication even when the endpoints themselves are fine.

Advantages of NAT, excluding address multiplexing, include:

- It hides internal addresses from the external network.
- It provides a simple filtering effect because unmatched inbound traffic is dropped.
- It lets the internal address plan stay stable even if the external address changes.

Disadvantages of NAT include:

- It breaks direct end-to-end reachability for unsolicited inbound traffic.
- It adds extra state and protocol complexity to the network path.
- It makes debugging harder because failures may be caused by hidden NAT state.

## 6. References

1. UNSW School of Computer Science and Engineering. *COMP3331/9331 26T1 Assignment Specification: Building a Network Address Translation System*. Term 1, 2026.
2. UNSW School of Computer Science and Engineering. *COMP3331/9331 26T1 Assignment Testing: Testing Your Network Address Translation System*. Term 1, 2026.
3. Postel, J. *RFC 791: Internet Protocol*. Internet Engineering Task Force, 1981.
4. Postel, J. *RFC 768: User Datagram Protocol*. Internet Engineering Task Force, 1980.
5. Postel, J. *RFC 792: Internet Control Message Protocol*. Internet Engineering Task Force, 1981.
