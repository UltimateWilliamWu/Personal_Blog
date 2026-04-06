## 1. Code Organisation

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

The most important data structure is the translation table. It is used to store the NAT state of active UDP flows. Each flow is stored in a NatMapping object, which contains the internal IP address, the internal port, the translated external port, and the time when the mapping was last used. The table stores two entries for the same mapping. One table handles outgoing lookups by internal IP address and internal port, while the other handles incoming lookups by external port. A double-ended queue (deque) is used to store currently inactive external ports. This enables fast bidirectional communication lookups within the NAT and allows ports to be reused once they have expired.

Fragment reassembly uses a separate table because it addresses a different problem. FragmentGroup stores the initial header, the expected total payload length, the time of the last update, and a payload mirror indexed by byte offset for the fragments.

ReassemblyTable indexes these groups (by interface name and identifier). As more fragments arrive, this table stores enough information to determine when reassembly is complete. Once all byte ranges have been found, the fragments are merged into a single IPv4Packet. Packet classes are also part of the data model. IPv4Packet, UDPSegment, and ICMPMessage store protocol fields not as raw bytes, but in a structured format. This provides a clear and concrete representation of the packet being processed at runtime, which greatly facilitates tasks such as header rewriting, checksum calculation, and ICMP generation.
The figure below summarises the two main state structures used by the NAT.

<div align="center">
  <img src="Pasted%20image%2020260406182407.png" width="1500">
  <div><em>Figure 2. Main NAT data structures.</em></div>
</div>

## 3. Concurrency Handling

This NAT uses an event-based, single-threaded model instead of a multithreaded one. Both UDP sockets are configured in non-blocking mode and registered with the DefaultSelector. The execution loop first cleans up expired NAT and fragmentation states, then waits for activity on one of the sockets; as soon as a socket becomes ready, it immediately processes packets.

The purpose of this model is to enable NAT to respond separately to ingress and egress traffic without requiring prior prediction of fixed request-response sequences. Input packets can arrive continuously even while output responses are being processed; conversely, output packets can be processed even when no new input packet has been detected. Since all shared states are updated within a single execution path, this implementation avoids locks and race conditions.

## 4. Known Limitations

This implementation follows the assignment model rather than a full production NAT. It only supports IPv4 packets with a fixed 20-byte header, UDP traffic, and the ICMP behaviour required by the specification. It does not support IP options or a wider range of transport protocols.

The simplified runtime model also introduces a few practical assumptions. The internal network is represented by one real UDP client endpoint, so replies to the internal side are sent to the most recently seen client address. Generated ICMP error packets use the configured external IP as their source address because the assignment does not define a separate logical internal NAT address. Fragment reassembly also follows the specification assumption that identification values are globally unique, which allows a simpler reassembly key.

## 5. Discussion

NAT is extremely useful in practical applications, but it does not fully comply with the principles of the traditional Internet architecture. From a hierarchical architectural perspective, NAT cannot function like a simple IP router. After modifying the packet, it is necessary to check the UDP header, rewrite the port number, and recalculate the UDP checksum. In other words, a network-layer device also makes changes at the transport layer. This violates the principle of network layer separation.

This also violates the end-to-end principle of NAT. By implementing address translation, the communication depends not only on the two endpoints but also on the internal state of the intermediate device. Incoming packets are accepted only if a corresponding mapping exists, and that mapping can be lost due to timeouts or port exhaustion. This means that NAT doesn't just forward packets along the path but actively influences the success or failure of communication sessions.

In addition to address reuse, NAT offers several specific practical advantages: it hides internal addresses from the external network, thereby preventing the direct exposure of the internal address space. Since it typically rejects traffic without a matching mapping, it automatically blocks unexpected incoming traffic and acts as a simple filter. It also preserves the stability of the internal naming scheme when the external address changes. However, its drawbacks are clear: it disrupts direct end-to-end connections and makes unexpected incoming traffic and peer-to-peer communication more difficult.

As a result, NAT introduces additional complexities such as maintaining association state, updating aggregate checks, and handling special cases of ICMP and fragmentation.This makes troubleshooting difficult, because connection errors may stem not from the end devices but from the underlying NAT state.

## 6. References

1. UNSW School of Computer Science and Engineering. *COMP3331/9331 26T1 Assignment Specification: Building a Network Address Translation System*. Term 1, 2026.
2. UNSW School of Computer Science and Engineering. *COMP3331/9331 26T1 Assignment Testing: Testing Your Network Address Translation System*. Term 1, 2026.
3. Postel, J. *RFC 791: Internet Protocol*. Internet Engineering Task Force, 1981.
4. Postel, J. *RFC 768: User Datagram Protocol*. Internet Engineering Task Force, 1980.
5. Postel, J. *RFC 792: Internet Control Message Protocol*. Internet Engineering Task Force, 1981.
