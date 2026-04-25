# COMP9331 Lectures 0-10 Exam Notes

Source scope（资料范围）: this note is based on the lecture PDFs whose filenames start with `0` to `10` in `Lectures`. There is no `6.*.pdf` file in the folder, so Lecture 6 content is not invented here.

Use this note as an exam checklist（考试清单）: know the definition, know the formula, know which assumption the question is using, then compute or justify.

## 0. Course Introduction

### Core Purpose

- Computer networks（计算机网络） explain what happens when an application communicates over the Internet.
- Opening a web page involves DNS lookup（域名解析）, TCP connection setup（TCP 建连）, HTTP request/response（HTTP 请求响应）, routing（路由）, packet switching（分组交换）, delay/loss（时延和丢包）, and congestion control（拥塞控制）.
- The course learning model is Concept -> Observe -> Build（概念 -> 观察 -> 实现）.
- Labs use Wireshark/NS3 to observe real protocol behaviour（用抓包和仿真观察协议）.

### Assessment

- Labs: 20%.
- Assignment: 20%, usually implementation-oriented, such as an HTTP-related task.
- Midterm: 20%.
- Final exam: 40%.
- Final exam hurdle（期末门槛）: at least 40% in the final exam.
- Overall pass requirement（总评通过）: at least 50% overall.

### Exam Focus

- Do not treat protocols as memorised names only. You need to explain what each layer does, what fields are used, and how timing/queueing/retransmission changes behaviour.
- Common exam pattern（常见考法）: a scenario gives packet size, rate, RTT, sequence numbers, or subnet prefix; you must compute delay, ACK number, throughput, routing path, or address range.

### Lecture Question

Original question: What happens when you open `google.com` in a browser?

How to solve（解题思路）:
- First map the name to an IP address using DNS.
- Then establish a TCP connection to the server or CDN edge.
- Then send HTTP/HTTPS requests and receive objects.
- Packets are forwarded hop by hop through routers.
- TCP handles reliability, flow control, and congestion control.

Answer:
- DNS resolves the hostname, TCP establishes transport connectivity, HTTP transfers the web objects, IP routers forward packets, and TCP reacts to delay/loss/congestion during the transfer.

## 1. Introduction to Computer Networks

### Internet Structure

- The Internet is a network of networks（互联网是网络的网络）.
- Hosts/end systems（主机/端系统） run applications at the network edge.
- Communication links（通信链路） connect devices and have transmission rates measured in bits per second.
- Packet switches（分组交换设备） include routers and switches.
- Protocols（协议） define message format, order, and actions on send/receive.
- ISP hierarchy（ISP 层级结构） exists because every access ISP directly connecting to every other ISP would require O(N^2) connections and does not scale.
- IXPs（Internet Exchange Points，互联网交换点） allow networks to peer and exchange traffic.
- Content-provider networks（内容提供商网络）, such as large CDN/cloud networks, connect close to users to reduce delay and transit cost.

### Network Edge and Access Networks

- Access network（接入网） connects end systems to the first router.
- Residential access（家庭接入） includes DSL, cable, fibre, and wireless.
- Institutional access（机构接入） often uses Ethernet and WiFi.
- Mobile access（移动接入） uses cellular networks.
- Important access properties（重要指标）: bandwidth, shared or dedicated medium, reliability, and delay.

### Packet Switching

- Packet switching（分组交换） divides messages into packets and forwards each packet through routers.
- Store-and-forward（存储转发） means a router receives the entire packet before forwarding it.
- Transmission delay（发送时延） is `d_trans = L / R`, where `L` is packet length in bits and `R` is link rate in bits/s.
- Propagation delay（传播时延） is `d_prop = d / s`, where `d` is link distance and `s` is propagation speed.
- Processing delay（处理时延） is time to check headers, bit errors, and determine output link.
- Queueing delay（排队时延） occurs when packets wait in a router buffer.
- Packet loss（丢包） happens when the buffer is full and arriving packets are dropped.

### Circuit Switching

- Circuit switching（电路交换） reserves resources end-to-end before communication.
- Frequency Division Multiplexing, FDM（频分复用） splits bandwidth into frequency bands.
- Time Division Multiplexing, TDM（时分复用） splits time into slots.
- Circuit switching gives predictable rate but wastes resources for bursty traffic（突发流量下浪费资源）.

### Statistical Multiplexing

- Statistical multiplexing（统计复用） shares link capacity on demand.
- It works well when users are bursty and not all active simultaneously.
- Example from lecture: a 1 Mbps link, each user needs 100 kbps when active and is active 10% of the time.
- Circuit switching supports only 10 active users.
- Packet switching can support many more users statistically; with 35 users, the probability that more than 10 are active is about 0.0004.
- Use the binomial formula（用二项分布）: `P(k active) = C(N,k)p^k(1-p)^(N-k)`.

### Traffic Intensity and Queueing

- Traffic intensity（流量强度） is `rho = La / R`, where `L` is packet size in bits, `a` is average arrival rate in packets/s, and `R` is transmission rate.
- If `rho` approaches 1, queueing delay grows rapidly.
- If `La > R`, packets arrive faster than the link can transmit them, so the queue grows without bound until packets are dropped.
- Burstiness（突发性） matters even if the average arrival rate is below service rate; packets arriving close together can temporarily create queues.

### Throughput

- Throughput（吞吐量） is the rate at which bits are delivered end-to-end.
- Instantaneous throughput（瞬时吞吐量） is the rate at a particular moment.
- Average throughput（平均吞吐量） is total delivered bits divided by total transfer time.
- Bottleneck link（瓶颈链路） determines end-to-end throughput: `throughput = min(R1, R2, ..., Rn)`.

### Exam Focus

- Always distinguish transmission delay from propagation delay.
- Packet size affects transmission delay but not propagation delay.
- Distance affects propagation delay but not transmission delay.
- Queueing delay is the most variable delay and is strongly related to traffic intensity and burstiness.
- Circuit switching reserves resources; packet switching allocates resources on demand.
- In packet switching, different packets can experience different queueing delays.

### Lecture Questions

Original question: What is the Internet?

How to solve:
- Decide whether the statement describes the Internet as physical infrastructure, a service platform, or a single homogeneous network.

Answer:
- The Internet is an interconnection of networks（网络互联） and an infrastructure that provides services to distributed applications. It is not one homogeneous network.

Original question: In ______ resources are allocated on demand.

How to solve:
- Circuit switching reserves resources before transmission.
- Packet switching uses resources when packets arrive.

Answer:
- Packet switching.

Original question: In a circuit switched network, packet Y's path is ____ packet X's path.

How to solve:
- A circuit is fixed once established.

Answer:
- The same as packet X's path.

Original question: Does propagation delay depend on packet size?

How to solve:
- Use `d_prop = d / s`; packet length `L` is not in the formula.

Answer:
- No. Propagation delay depends on distance and propagation speed, not packet size.

Original question: What is the order of delays experienced at a router?

How to solve:
- A packet is examined, may wait, is pushed onto the link, then travels through the medium.

Answer:
- Processing delay -> queueing delay -> transmission delay -> propagation delay.

Original question: Five packets arrive simultaneously to an empty link. Each packet is 500 bytes, link rate is 4 Mbps, one packet at a time. What is the average queueing delay?

How to solve:
- Packet transmission time is `500 * 8 / 4,000,000 = 0.001 s = 1 ms`.
- Queueing delays are `0, 1, 2, 3, 4 ms`.
- Average is `(0+1+2+3+4)/5 = 2 ms`.

Answer:
- 2 ms.

Original question: Two arrival patterns have the same average rate below the router service rate. Which pattern gives higher average queueing delay?

How to solve:
- Compare burstiness（突发程度） rather than only the average.
- A pattern with packets clustered together can temporarily exceed service rate and build a queue.

Answer:
- The more bursty pattern gives higher average queueing delay because packets arrive close together and create queue buildup.

## 2. Application Layer Part 1: HTTP and Email

### Layering

- The Internet protocol stack（互联网协议栈） has application, transport, network, link, and physical layers.
- Application layer（应用层） supports network applications such as web, email, DNS, and P2P.
- Transport layer（传输层） provides process-to-process communication.
- Network layer（网络层） moves datagrams host-to-host.
- Link layer（链路层） moves frames over one link.
- Physical layer（物理层） moves bits over the medium.
- Layering benefits（分层好处）: modularity, independent evolution, easier troubleshooting.
- Layering drawbacks（分层代价）: duplicate functions, hidden information, and extra headers.

### Application Architectures

- Client-server architecture（客户-服务器架构） has always-on servers and clients that initiate communication.
- P2P architecture（对等架构） has peers that act as both clients and servers.
- A process（进程） communicates through sockets.
- A socket（套接字） is the interface between application and transport layer.
- A process is identified by IP address plus port number（IP 地址加端口号标识进程）.

### Application-Layer Protocols

- An application-layer protocol defines message types（消息类型）, message syntax（语法）, message semantics（语义）, and timing/rules（时序和规则）.
- Open protocols（开放协议） are publicly specified, such as HTTP and SMTP.
- Proprietary protocols（私有协议） are controlled by vendors.

### Transport Service Requirements

- Data integrity（数据完整性） means no loss/corruption.
- Timing（时延要求） matters for real-time applications.
- Throughput（吞吐需求） matters for bandwidth-sensitive applications.
- Security（安全性） can be provided by encryption/authentication, often above TCP/UDP.

### TCP and UDP Service Models

- TCP provides reliable data transfer（可靠传输）, flow control（流量控制）, congestion control（拥塞控制）, and connection-oriented service（面向连接服务）.
- TCP does not guarantee timing, minimum throughput, or built-in security.
- UDP provides best-effort unreliable datagram service（尽力而为的不可靠数据报服务）.
- UDP has no setup delay, small header, no flow control, and no congestion control.

### HTTP Basics

- HTTP is the Web's application-layer protocol（Web 的应用层协议）.
- A web page consists of a base HTML file（基础 HTML 文件） plus referenced objects（引用对象）.
- HTTP uses TCP, usually port 80 for HTTP and 443 for HTTPS.
- HTTP is stateless（无状态）: the server does not maintain client request history by default.
- HTTP request methods include GET, POST, and HEAD.
- HTTP messages are human-readable text in classic HTTP/1.x.
- A request line includes method, URL, and version, such as `GET /index.html HTTP/1.1`.
- Headers carry metadata such as Host, User-Agent, Accept, Cookie, and Connection.
- The body is used for POST data and some responses.

### Cookies

- Cookies（Cookie） allow web sites to maintain state over stateless HTTP.
- Server sends `Set-Cookie`.
- Browser stores cookie.
- Browser sends `Cookie` header in later requests.
- Server can map the cookie to backend database state.
- Cookies support sessions, login, shopping carts, and tracking.

### HTTP Performance

- Page Load Time, PLT（页面加载时间） depends on object count, object size, RTT, bandwidth, TCP setup, and parallelism.
- Non-persistent HTTP（非持久 HTTP） opens a new TCP connection for each object.
- Persistent HTTP（持久 HTTP） reuses the same TCP connection for multiple objects.
- HTTP/1.1 without pipelining sends a new request only after the previous response.
- HTTP/1.1 with pipelining sends multiple requests back-to-back.
- HTTP/2 reduces application-layer head-of-line blocking using multiplexed streams over one TCP connection.

### HTTP Timing Formulas

Let `D` be RTT, `S0` be base HTML size, `S` be each referenced object size, `C` be link rate, and `N` be number of referenced objects.

- Non-persistent HTTP without parallel connections:
  `2D + S0/C + N(2D + S/C)`.
- Persistent HTTP without pipelining:
  `2D + S0/C + N(D + S/C)`.
- Persistent HTTP with pipelining:
  `3D + S0/C + NS/C`.

### Web Caching

- Web cache/proxy（Web 缓存/代理） stores copies of objects near clients.
- Cache hit（缓存命中） means the object is served locally.
- Cache miss（缓存未命中） means the cache fetches from origin server.
- Conditional GET（条件 GET） uses `If-Modified-Since`.
- If unchanged, server returns `304 Not Modified`.
- If changed, server returns `200 OK` with the object.
- Caching reduces access-link traffic and user delay.

### CDN and Replication

- Content Distribution Networks, CDN（内容分发网络） replicate content near users.
- DNS can map users to different CDN servers based on location, load, and network conditions.
- Pull caching（拉取缓存） fetches content on demand.
- Push replication（推送复制） places content in advance.

### Email

- Email path: user agent -> sender mail server -> receiver mail server -> receiver mailbox -> receiver user agent.
- SMTP（Simple Mail Transfer Protocol，简单邮件传输协议） transfers mail between mail servers.
- SMTP uses TCP port 25.
- SMTP is push-based（发送方推送）.
- SMTP uses commands such as `HELO`, `MAIL FROM`, `RCPT TO`, `DATA`, and `QUIT`.
- SMTP responses are status code plus phrase.
- Traditional SMTP uses 7-bit ASCII format.
- Mail access protocols（邮件访问协议） include POP3, IMAP, and HTTP-based webmail.

### Exam Focus

- If a question asks for number of RTTs, separate TCP handshake, HTTP request, response arrival, and object transfer.
- For HTTP/1.1 persistent connection, the base file must be downloaded before the browser knows referenced objects.
- Parallel TCP connections reduce object wait time but can overload networks and are unfair to other users.
- For cache questions, compute access-link utilization first; high utilization near 1 means queueing dominates.

### Lecture Questions

Original question: Which statement about TCP and UDP is true?

How to solve:
- Compare service guarantees, not application examples.

Answer:
- TCP provides reliable data transfer while UDP does not.

Original question: A webpage has base HTML of size `S0` bits and `N` inline objects each of size `S` bits. RTT is `D`, link rate is `C`. What is the response time for non-persistent HTTP with no parallelism?

How to solve:
- Base object needs TCP setup + HTTP request/first byte = 2RTT, plus transmission.
- Each referenced object uses a new TCP connection and also needs 2RTT plus transmission.

Answer:
- `2D + S0/C + N(2D + S/C)`.

Original question: Same webpage, persistent HTTP without pipelining. What is the response time?

How to solve:
- Base object still needs 2RTT plus transmission.
- Each referenced object needs one additional RTT plus transmission because requests are sequential.

Answer:
- `2D + S0/C + N(D + S/C)`.

Original question: Same webpage, persistent HTTP with pipelining. What is the response time?

How to solve:
- Base object needs 2RTT plus transmission.
- After parsing base HTML, one RTT gets the first bytes of all pipelined referenced objects.
- Then transmit all referenced objects.

Answer:
- `3D + S0/C + NS/C`.

Original question: A webpage has 10 referenced objects on the same server. HTTP/1.1 without pipelining opens one parallel TCP connection per object only after the base file is downloaded. One TCP handshake takes one RTT. Ignore closing overhead. How many RTTs are needed?

How to solve:
- Base HTML: 1 RTT handshake + 1 RTT request/response = 2 RTT.
- After base is known, all 10 object connections are parallel: 1 RTT handshake + 1 RTT request/response = 2 RTT total, not 20.

Answer:
- 4 RTTs.

Original question: A webpage has 7 referenced objects. HTTP/1.1 with pipelining uses one TCP connection. How many RTTs are needed?

How to solve:
- One TCP handshake is 1 RTT.
- Base page request/response is 1 RTT.
- Pipelined referenced objects need 1 more RTT after base HTML is known.

Answer:
- 3 RTTs.

Original question: An enterprise LAN sends 15 requests/s, average object size 100 Kbits, access link rate 1.5 Mbps. Which delay dominates?

How to solve:
- Arrival bit rate is `15 * 100,000 = 1,500,000 bps`.
- Traffic intensity is `1,500,000 / 1,500,000 = 1`.
- At utilization near 1, queueing delay grows very large.

Answer:
- Queueing delay at the gateway dominates because the access link is fully utilised.

## 3. Application Layer Part 2: DNS, P2P, CDN, Sockets

### DNS Motivation

- DNS（Domain Name System，域名系统） maps hostnames to IP addresses.
- A centralized DNS database would not scale because of single point of failure, huge traffic volume, long distance to users, and difficult maintenance.
- DNS is distributed and hierarchical（分布式层级系统）.

### DNS Services

- Hostname-to-IP translation（主机名到 IP 地址解析）.
- Host aliasing（主机别名） through CNAME records.
- Mail server aliasing（邮件服务器别名） through MX records.
- Load distribution（负载分配） by returning different IP addresses.

### DNS Hierarchy

- Root DNS servers（根 DNS 服务器） know TLD servers.
- Top-Level Domain, TLD servers（顶级域服务器） know authoritative servers for domains such as `.com`, `.edu`, `.au`.
- Authoritative DNS servers（权威 DNS 服务器） store records for a domain.
- Local DNS server（本地 DNS 服务器） is usually provided by ISP, university, or enterprise and acts as proxy/cache.

### Iterative and Recursive Queries

- Iterative query（迭代查询）: a DNS server replies with the next DNS server to ask.
- Recursive query（递归查询）: a DNS server resolves the full answer on behalf of the requester.
- Recursive service gives more work to the contacted DNS server.

### DNS Caching

- DNS caching（DNS 缓存） stores records for future queries.
- TTL（Time To Live，生存时间） controls how long records are cached.
- Caching improves performance but can return stale records until TTL expires.
- Negative caching（负缓存） can store failed lookup results.

### DNS Resource Records

- DNS RR format is `(name, value, type, ttl)`.
- `A`: name is hostname, value is IPv4 address.
- `NS`: name is domain, value is authoritative DNS server hostname.
- `CNAME`: name is alias hostname, value is canonical hostname.
- `MX`: name is domain, value is mail server hostname.

### DNS Registration

- A domain owner registers a domain with a registrar.
- Registrar inserts NS and glue A records into the TLD system.
- The domain's authoritative DNS server stores A, CNAME, MX, and other records.

### DNS Security

- DNS cache poisoning（DNS 缓存投毒） inserts false mappings into caches.
- A mitigation is to cache only authoritative mappings and validate responses.

### P2P and BitTorrent

- P2P（peer-to-peer，对等网络） has peers that both request and provide data.
- P2P is self-scalable（自扩展） because each peer adds upload capacity.
- Peers are intermittently connected（间歇在线） and may change IP addresses.
- In BitTorrent, a file is divided into chunks（文件块）, often 256 KB in the lecture model.
- Tracker（跟踪器） tells a new peer which peers are in the torrent.
- Rarest-first（最稀有优先） chooses chunks that are least replicated among neighbours.
- Tit-for-tat（以牙还牙） uploads to peers that currently provide the best download rate.
- Optimistic unchoking（乐观解封） occasionally uploads to a random peer to discover better partners.

### CDN

- Video traffic is large and delay-sensitive, so a single mega-server is not scalable.
- CDN stores content at multiple geographically distributed sites.
- Deep CDN（深入式 CDN） places servers inside many access networks.
- Bring-home CDN（集中式 CDN） uses large clusters near major IXPs.
- CDN DNS redirection maps users to suitable CDN servers.

### UDP Socket Programming

- A socket is the door between application and transport layer（应用和传输层之间的门）.
- UDP server creates a socket and binds to a port.
- UDP client sends datagrams to server IP and port.
- Server uses `recvfrom` to learn client IP and port, then replies using `sendto`.
- UDP has message boundaries; each send creates a datagram.

### Exam Focus

- For DNS record type questions, identify what the `name` and `value` fields mean.
- For DNS query count questions, state cache assumption.
- For BitTorrent questions, "download first" usually means rarest-first, not random or largest chunk.
- CDN questions often ask what the CDN authoritative DNS server does.

### Lecture Questions

Original question: A client only knows the domain name but no DNS information is cached. Which server does the local DNS server ask first?

How to solve:
- DNS resolution starts at the root when no cache can help.

Answer:
- The root DNS server.

Original question: Which DNS servers are maintained by the client-side ISP and by the domain owner?

How to solve:
- Client-side ISP provides local DNS resolver.
- Domain owner controls authoritative DNS records.

Answer:
- Local DNS server is maintained by the client-side ISP; authoritative DNS server is maintained by the domain owner.

Original question: Sending email to `mahbub@unsw.edu.au` triggers which DNS query type?

How to solve:
- Email needs the mail server for a domain, not just a host IP.

Answer:
- MX query.

Original question: Browser visits `www.pollev.com`. What is the minimum number of DNS requests made by the local DNS server?

How to solve:
- If the local DNS cache already has the answer, zero external DNS requests are needed.
- If no cache is assumed, iterative resolution normally asks root, TLD, and authoritative DNS, so three external DNS requests are needed.

Answer:
- With cache allowed by the word "minimum": 0. With the common no-cache exam assumption: 3. State the assumption.

Original question: A DNS resource record has `cse.unsw.edu.au` in the name field and `dns.cse.unsw.edu.au` in the value field. Which type is likely?

How to solve:
- A domain name mapped to a DNS server hostname is an NS record.

Answer:
- NS.

Original question: In BitTorrent, what does tit-for-tat determine?

How to solve:
- Tit-for-tat is about upload partner selection, not chunk choice.

Answer:
- It determines to which peers a node uploads chunks.

Original question: Alice joins a torrent with chunks held by peers. Which chunk should she download first?

How to solve:
- Count how many peers hold each chunk.
- Select a rarest chunk among those available.
- If multiple chunks are equally rare, any of them is acceptable.

Answer:
- Download a chunk that appears at the fewest peers, because BitTorrent uses rarest-first to improve availability and reduce the chance that a chunk disappears.

Original question: What is the role of the CDN authoritative DNS server?

How to solve:
- CDN DNS does not directly send the video object; it chooses a CDN server.

Answer:
- It maps the client's DNS query to a suitable CDN server, often based on proximity, load, and network conditions.

## 4. Transport Layer Part 1: UDP and Reliable Data Transfer

### Multiplexing and Demultiplexing

- Multiplexing（复用） gathers data from multiple sockets and adds transport headers.
- Demultiplexing（分用） uses header fields to deliver received segments to the correct socket.
- UDP demultiplexing mainly uses destination IP address and destination port.
- TCP demultiplexing uses the 4-tuple: source IP, source port, destination IP, destination port.

### UDP

- UDP provides connectionless transport（无连接传输）.
- UDP segments may be lost, duplicated, or delivered out of order.
- UDP has no congestion control, so it can continue sending even under congestion.
- UDP has small header overhead.
- Applications can build reliability or congestion control at application layer if needed.
- Common UDP applications include DNS, DHCP, SNMP, streaming media, gaming, and HTTP/3/QUIC.

### UDP Header and Checksum

- UDP header fields: source port, destination port, length, checksum.
- UDP checksum（UDP 校验和） detects errors over UDP header, data, and pseudo-header.
- Sender computes one's complement sum（反码和） over 16-bit words.
- Receiver recomputes checksum; a mismatch detects an error.
- Checksum can miss some errors because different bit errors can cancel out.

### Reliable Data Transfer Models

- `rdt1.0`: reliable transfer over a perfectly reliable channel.
- `rdt2.0`: handles bit errors using checksum, ACK, NAK, and retransmission.
- `rdt2.0` fatal flaw: corrupted ACK/NAK can make the sender take the wrong action.
- `rdt2.1`: adds sequence numbers to detect duplicates.
- `rdt2.2`: removes NAK; receiver sends ACK for the last correctly received packet.
- `rdt3.0`: handles packet loss using timeout and retransmission.

### Stop-and-Wait Performance

- Stop-and-wait（停止等待） sends one packet and waits for its ACK.
- Sender utilisation（发送方利用率） is:
  `U_sender = (L/R) / (RTT + L/R)`.
- Large RTT and small packet transmission time make stop-and-wait inefficient.
- Pipelining（流水线） allows multiple packets in flight and increases utilisation.

### Go-Back-N

- Go-Back-N, GBN（回退 N） allows up to `N` unacknowledged packets.
- Sender has a window of sequence numbers.
- Receiver accepts only in-order packets.
- Receiver discards out-of-order packets and sends duplicate ACK for the last in-order packet.
- GBN uses cumulative ACKs（累计确认）.
- GBN usually has one timer for the oldest unacknowledged packet.
- On timeout, sender retransmits the timed-out packet and all later packets in the window.
- For `k` sequence number bits, sequence space is `2^k`; common GBN safety condition is `N <= 2^k - 1`.

### Selective Repeat

- Selective Repeat, SR（选择重传） individually ACKs correctly received packets.
- Receiver buffers out-of-order packets.
- Sender retransmits only packets that time out.
- SR needs one timer per outstanding packet.
- To avoid ambiguity after sequence number wraparound, `window size <= half sequence space`.
- For `k` bits, maximum SR window is `2^(k-1)`.

### Exam Focus

- GBN receiver discards out-of-order data; SR receiver buffers out-of-order data.
- GBN retransmits a block; SR retransmits individual missing packets.
- Stop-and-wait needs only two sequence numbers because only one packet can be outstanding.
- If ACKs can be lost, timeout is necessary.
- If packets can be corrupted, checksum is necessary.
- If retransmissions can create duplicates, sequence numbers are necessary.

### Lecture Questions

Original question: 100 UDP clients communicate with a UDP web server. Requests and responses fit in one segment. How many sockets does the server need and how many does each client need?

How to solve:
- UDP server can receive all clients on one socket bound to the server port.
- Each client can use one UDP socket.

Answer:
- Server: 1 socket. Each client: 1 socket.

Original question: 100 TCP clients communicate with a traditional HTTP/TCP web server. How many sockets does the server need and how many does each client need?

How to solve:
- Server has one listening socket plus one connection socket per client.
- Each client has one connection socket.

Answer:
- Server: 101 sockets. Each client: 1 socket.

Original question: Do all TCP sockets at the server have the same server-side port?

How to solve:
- TCP connections are distinguished by the 4-tuple.

Answer:
- Yes. They can share the same server port because source IP and source port differ across clients.

Original question: For corruption only, with no packet loss or reordering, which mechanisms are strictly needed?

How to solve:
- Corruption requires error detection.
- Sender needs feedback to know whether to retransmit.

Answer:
- Checksums, ACKs, and NAKs.

Original question: If packets, ACKs, and NAKs can be lost, what happens to rdt2.1 or rdt2.2?

How to solve:
- Without timeout, a lost control packet can leave the sender waiting forever.

Answer:
- The protocol can get stuck, so timeout is needed.

Original question: For corruption and loss, which mechanisms are strictly needed?

How to solve:
- Corruption needs checksum.
- Loss needs timeout.
- Duplicates from retransmissions need sequence numbers.
- ACKs are needed for progress.

Answer:
- Checksums, ACKs, timeouts, and sequence numbers.

Original question: Which statement is not true about Go-Back-N?

How to solve:
- GBN uses one timer for the oldest unacknowledged packet, not one timer for every packet.

Answer:
- "GBN maintains a separate timer for each outstanding packet" is not true.

Original question: Receiver has correctly received all packets up to 24, then receives packets 27 and 28. What ACKs are sent in GBN and SR?

How to solve:
- GBN discards out-of-order packets and repeats ACK for last in-order packet.
- SR individually ACKs out-of-order packets.

Answer:
- GBN sends ACK 24 and ACK 24. SR sends ACK 27 and ACK 28.

Original question: Go-Back-N window size is 600. The sequence number field must have at least how many bits?

How to solve:
- GBN needs sequence space at least `N+1`.
- Need `2^k >= 601`.
- `2^9 = 512`, `2^10 = 1024`.

Answer:
- 10 bits.

Original question: What is the maximum SR window size for a 16-bit sequence number field?

How to solve:
- SR maximum window is half of the sequence number space.
- Sequence space is `2^16 = 65536`.
- Half is `32768`.

Answer:
- 32768 packets.

## 5. Transport Layer Part 2: TCP

### TCP Basics

- TCP is connection-oriented（面向连接） and reliable（可靠）.
- TCP provides a byte stream（字节流）, not message boundaries.
- TCP segment sequence number（序列号） is the byte number of the first data byte in the segment.
- TCP ACK number（确认号） is the next byte expected by the receiver.
- TCP uses cumulative ACKs（累计 ACK）.
- Maximum Segment Size, MSS（最大报文段长度） is the largest TCP payload size.
- Typical Ethernet MSS is 1460 bytes because Ethernet MTU is 1500 and IP/TCP headers are usually 20 bytes each.
- TCP receiver may buffer out-of-order segments.
- TCP uses checksum, retransmission timer, duplicate ACKs, and fast retransmit.

### TCP Sequence and ACK Numbers

- SYN consumes one sequence number.
- FIN consumes one sequence number.
- Pure ACK with no data does not consume sequence space.
- If a data segment has sequence number 400 and 100 payload bytes, it carries bytes 400 through 499.
- If all bytes up to 499 are received in order, the ACK should be 500.
- If the receiver is still missing earlier byte 300, it keeps ACKing 300 even if bytes 400-499 arrive correctly.

### RTT Estimation and Timeout

- SampleRTT（样本 RTT） is measured from segment transmission until its ACK is received.
- TCP does not measure SampleRTT for retransmitted segments because of ACK ambiguity.
- EstimatedRTT（估计 RTT）:
  `EstimatedRTT = (1-alpha) * EstimatedRTT + alpha * SampleRTT`, with `alpha = 0.125`.
- DevRTT（RTT 偏差）:
  `DevRTT = (1-beta) * DevRTT + beta * |SampleRTT - EstimatedRTT|`, with `beta = 0.25`.
- TimeoutInterval（超时间隔）:
  `TimeoutInterval = EstimatedRTT + 4 * DevRTT`.

### TCP Flow Control

- Flow control（流量控制） prevents receiver buffer overflow.
- Receiver advertised window, rwnd（接收窗口）, tells sender how much free buffer space remains.
- Sender limits unacknowledged data so it does not exceed rwnd.
- If rwnd is zero, sender periodically sends small probes to learn when the window opens.

### TCP Connection Management

- Three-way handshake（三次握手）:
  SYN with `Seq = x`.
  SYNACK with `Seq = y, Ack = x+1`.
  ACK with `Seq = x+1, Ack = y+1`.
- First data byte from the TCP sender has sequence number `ISN + 1`.
- TCP close uses FIN segments.
- FIN consumes one sequence number.
- Common closure can be 4-segment `FIN, ACK, FIN, ACK`, 3-segment if FIN and ACK are combined, or simultaneous close.
- TIME_WAIT（等待状态） lets old duplicate segments expire and allows retransmission of final ACK.
- RST（复位） abruptly closes a connection and is not reliable like FIN.

### TCP Congestion Control

- Congestion control（拥塞控制） protects the network from overload.
- TCP sender window is constrained by `min(cwnd, rwnd)`.
- Congestion window, cwnd（拥塞窗口）, controls how much data can be in flight.
- Approximate TCP sending rate is `cwnd / RTT`.
- Slow start（慢启动） begins with small cwnd and doubles cwnd every RTT.
- In slow start, cwnd increases by 1 MSS for every ACK.
- Congestion avoidance（拥塞避免） increases cwnd roughly by 1 MSS per RTT.
- Additive Increase Multiplicative Decrease, AIMD（加性增、乘性减） probes for bandwidth and backs off after loss.
- Timeout is treated as severe congestion: set `ssthresh = cwnd/2`, set `cwnd = 1 MSS`, restart slow start.
- Triple duplicate ACK（三个重复 ACK） indicates likely isolated loss and triggers fast retransmit.
- TCP Tahoe sets cwnd to 1 after triple duplicate ACK.
- TCP Reno halves cwnd after triple duplicate ACK and uses fast recovery.

### Exam Focus

- ACK number is next expected byte, not last received byte.
- A receiver can ACK 300 after receiving bytes 400-499 if byte 300 is still missing.
- ISN plus SYN means first data sequence number is `ISN + 1`.
- Flow control protects receiver buffer; congestion control protects network/router buffers.
- Timeout and triple duplicate ACK produce different cwnd responses.
- When reading a cwnd graph, exponential growth indicates slow start; linear growth indicates congestion avoidance; drop to 1 indicates timeout; halving indicates triple duplicate ACK/Reno.

### Lecture Questions

Original question: TCP sender sends a 100-byte segment with sequence number 1234 and ACK number 436. What is the highest sequence number the sender has received from the other side?

How to solve:
- ACK 436 means the next expected byte is 436.
- Therefore all bytes through 435 have been received.

Answer:
- 435.

Original question: TCP Reno handshake completes with sender ISN 256. The first data segment carries 20 bytes. What is the sequence number of the first data segment?

How to solve:
- SYN consumes one sequence number.
- First data byte starts at ISN + 1.

Answer:
- 257.

Original question: Host A sends a 100-byte TCP segment carrying sequence number 400 to Host B. Host B receives it correctly and sends ACK 300. Explain a scenario where this happens.

How to solve:
- Bytes 400-499 were received.
- But TCP ACKs the next expected in-order byte.
- If byte 300 or the segment starting at 300 was lost earlier, the receiver is still waiting for byte 300.

Answer:
- Host B can ACK 300 if it has not yet received byte 300 in order. The segment 400-499 is out of order, so B may buffer it but still sends cumulative ACK 300.

Original question: TCP uses flow control to ensure that the:

How to solve:
- Flow control concerns the receiver, not routers or congestion window.

Answer:
- Receiver's buffer does not overflow.

Original question: Which TCP Reno statement is correct?

How to solve:
- TCP Reno retransmits on timeout or after triple duplicate ACKs.
- "Same ACK three times" in common exam wording means receiving three duplicate ACKs.

Answer:
- TCP Reno retransmits after receiving the same ACK three times.

Original question: EstimatedRTT is 100 ms and SampleRTT is 108 ms. What happens?

How to solve:
- New sample is larger than old estimate, so EstimatedRTT increases.
- Timeout also depends on DevRTT, so it is not determined by EstimatedRTT alone.

Answer:
- EstimatedRTT increases; whether TimeoutInterval increases depends on the deviation term.

Original question: In a TCP cwnd graph, how do you identify a timeout versus triple duplicate ACK?

How to solve:
- Timeout drops cwnd to 1 MSS.
- Triple duplicate ACK in Reno roughly halves cwnd.

Answer:
- Drop to 1 MSS indicates timeout; halving indicates triple duplicate ACK/fast retransmit.

## 7. Network Layer: Data Plane

### Data Plane and Control Plane

- Forwarding（转发） is the local router action of moving a packet from input port to output port.
- Routing（路由） is the network-wide process of determining end-to-end paths.
- Data plane（数据平面） performs forwarding.
- Control plane（控制平面） computes and installs forwarding tables.

### IP Datagram Header

- Version identifies IPv4 or IPv6.
- Header length gives IP header length in 32-bit words.
- Type of Service / DS field can support differentiated service.
- Total length is the full IP datagram length.
- Identification, flags, and fragment offset support fragmentation.
- TTL（Time To Live，生存时间） prevents forwarding loops and is decremented at each router.
- Protocol field tells the destination host which upper-layer protocol to deliver to, such as TCP or UDP.
- Header checksum detects errors in the IP header only.
- Source and destination IP addresses identify interfaces.
- Options are optional and rarely used.

### IP Fragmentation

- MTU（Maximum Transmission Unit，最大传输单元） is the largest link-layer frame payload.
- If an IP datagram is larger than MTU, IPv4 can fragment it.
- Fragmentation may happen at routers.
- Reassembly happens only at the final destination.
- Fragment offset is measured in 8-byte units.
- All fragments except the last must carry a data size that is a multiple of 8 bytes.
- More Fragments, MF（更多分片标志） is 1 for non-final fragments and 0 for the final fragment.

### Fragmentation Example

Original problem: 4000-byte IP datagram, 20-byte IP header, MTU 1500 bytes.

How to solve:
- Original data is `4000 - 20 = 3980` bytes.
- Each full fragment can carry `1500 - 20 = 1480` bytes, and 1480 is divisible by 8.
- Remaining data after two full fragments is `3980 - 2960 = 1020`.
- Offsets are `0`, `1480/8 = 185`, and `2960/8 = 370`.

Answer:
- Fragment 1: length 1500, offset 0, MF 1.
- Fragment 2: length 1500, offset 185, MF 1.
- Fragment 3: length 1040, offset 370, MF 0.

### IP Addressing and Subnets

- An IP address identifies an interface（接口）, not an entire host.
- A subnet（子网） is a set of interfaces that can physically reach each other without passing through a router.
- CIDR（Classless Inter-Domain Routing，无类别域间路由） uses prefix notation `a.b.c.d/x`.
- Prefix length `x` gives the number of network bits.
- Number of addresses in a prefix is `2^(32-x)`.
- Network address has all host bits 0.
- Broadcast address has all host bits 1.
- Usable host addresses are usually total addresses minus 2 for IPv4 subnets.

### Longest Prefix Match

- Longest Prefix Match, LPM（最长前缀匹配） chooses the forwarding table entry with the most specific matching prefix.
- More-specific routes override less-specific aggregate routes.
- Route aggregation（路由聚合） reduces forwarding table size.

### DHCP

- DHCP（Dynamic Host Configuration Protocol，动态主机配置协议） assigns host IP configuration.
- DHCP Discover: client broadcasts to find server.
- DHCP Offer: server offers address and configuration.
- DHCP Request: client requests offered address.
- DHCP ACK: server confirms lease.
- DHCP can also provide subnet mask, default gateway, and DNS server.
- DHCP uses UDP port 67 on server and UDP port 68 on client.

### NAT

- NAT（Network Address Translation，网络地址转换） maps private internal addresses to public addresses.
- Private IPv4 ranges include `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.
- NAT changes outgoing source IP/port and incoming destination IP/port.
- NAT table records internal address/port and external mapped address/port.
- NAT conserves public IPv4 addresses and hides internal hosts.
- NAT breaks the pure end-to-end model and complicates inbound connections.
- NAT traversal can use port forwarding, UPnP, STUN-like methods, or relays.

### ICMP

- ICMP（Internet Control Message Protocol，互联网控制报文协议） carries error and control messages.
- Ping uses ICMP echo request/reply.
- Traceroute uses TTL expiry and ICMP time exceeded messages.

### Exam Focus

- Fragment offset is in 8-byte units, not bytes.
- IP checksum covers only the IP header, not payload.
- DHCP uses broadcast before the client has a configured IP.
- Longest prefix match means a more-specific `/24` beats a less-specific `/16`.
- NAT table entries are needed so returning packets can be mapped back to the correct internal host.

### Lecture Questions

Original question: A class C network `201.70.64.0` must be divided into at least six subnets. What subnet mask is needed?

How to solve:
- Six subnets require borrowing 3 bits because `2^2 = 4` is not enough and `2^3 = 8`.
- Class C default is `/24`; borrowing 3 bits gives `/27`.
- `/27` mask is `255.255.255.224`.

Answer:
- `/27`, or `255.255.255.224`.

Original question: How many addresses are in `128.119.254.0/25`?

How to solve:
- Host bits = `32 - 25 = 7`.
- Addresses = `2^7 = 128`.

Answer:
- 128 addresses, usually 126 usable host addresses.

Original question: How many addresses are in `134.45.22.0/23`?

How to solve:
- Host bits = `32 - 23 = 9`.
- Addresses = `2^9 = 512`.

Answer:
- 512 addresses.

Original question: Which fields are changed by NAT for outgoing packets?

How to solve:
- NAT maps private internal endpoint to public external endpoint.

Answer:
- Source IP address and usually source port are changed on outgoing packets; destination IP and destination port are changed back on incoming packets.

Original question: What does DHCP provide besides an IP address?

How to solve:
- DHCP configures host network settings.

Answer:
- Subnet mask, default gateway, DNS server, and lease information.

## 8. Routing

### Routing Overview

- Routing algorithm（路由算法） computes least-cost paths.
- Intra-domain routing（域内路由） happens within one autonomous system.
- Link cost（链路代价） can represent hop count, bandwidth, delay, or administrative cost depending on protocol.

### Link-State Routing

- Link-state routing（链路状态路由） gives every router a complete view of network topology and link costs.
- Routers flood link-state advertisements to all other routers.
- Each router runs Dijkstra's algorithm locally.
- Dijkstra variables:
  `N'` is the set of nodes with known least-cost path.
  `D(v)` is the current least cost from source to node `v`.
  `p(v)` is predecessor of `v` on the current path.
- Algorithm steps:
  initialise source and direct neighbours.
  repeatedly add the node with the smallest tentative `D(v)`.
  update costs through the newly added node.
- Result is a shortest-path tree and forwarding table.

### Distance-Vector Routing

- Distance-vector routing（距离向量路由） is distributed and iterative.
- Each router knows costs to neighbours and receives neighbours' advertised distance vectors.
- Bellman-Ford equation:
  `Dx(y) = min_v { c(x,v) + Dv(y) }`.
- Router `x` chooses the neighbour `v` that minimises path cost to destination `y`.
- Updates are asynchronous and can be triggered by changes.

### Count-to-Infinity Problem

- Count-to-infinity（数到无穷问题） happens when routers slowly increase path cost after a route failure due to incorrect neighbour information.
- Bad news travels slowly in distance-vector routing.
- Routing loops can occur during convergence.

### Split Horizon and Poison Reverse

- Split horizon（水平分割）: do not advertise a route back to the neighbour from which it was learned.
- Poison reverse（毒性反转）: advertise that route back with infinite cost.
- These reduce some loops but do not solve all distance-vector problems.

### Exam Focus

- Link-state: every router learns global topology, then computes paths.
- Distance-vector: routers know only neighbours and neighbour vectors.
- Dijkstra questions require table updates; do not jump straight to the final path without showing cost updates.
- Bellman-Ford questions require trying each neighbour as next hop.
- Link-state reacts differently from distance-vector after failures; distance-vector can have count-to-infinity.

### Lecture Questions

Original question: In link-state routing, what information is sent and to whom?

How to solve:
- Link-state advertisements describe directly connected link costs.
- They are flooded to all routers.

Answer:
- Each router sends information about its directly connected links to all nodes.

Original question: In distance-vector routing, what information is shared and with whom?

How to solve:
- A router sends its distance vector only to neighbours.

Answer:
- Each router shares its distance table/vector with all immediate neighbours.

Original question: What is the Bellman-Ford update rule?

How to solve:
- Evaluate every possible next-hop neighbour.

Answer:
- `Dx(y) = min_v { c(x,v) + Dv(y) }`.

Original question: Why can distance-vector routing converge slowly after a link failure?

How to solve:
- Neighbours may incorrectly believe each other still has a route.
- They repeatedly update cost upward.

Answer:
- Because of the count-to-infinity problem.

## 9. Link Layer

### Link Layer Services

- Link layer（链路层） transfers frames between neighbouring nodes over one link.
- Services can include framing, link access, reliable delivery on a link, flow control, error detection, and error correction.
- Not every link-layer protocol provides every service.

### Error Detection and Correction

- Single-bit parity（一维奇偶校验） detects an odd number of bit errors.
- Two-dimensional parity（二维奇偶校验） can detect and correct many single-bit errors.
- Checksum（校验和） is simple but weaker than CRC.
- Cyclic Redundancy Check, CRC（循环冗余校验） treats bits as polynomial coefficients.
- Sender appends remainder `R` so the transmitted bit string is divisible by generator `G`.
- Receiver divides by `G`; zero remainder means no detected error.
- CRC is strong for burst error detection but does not correct errors.

### Multiple Access Problem

- Broadcast channel（广播信道） is shared by multiple nodes.
- Collision（碰撞） occurs when multiple nodes transmit simultaneously and frames interfere.
- Ideal MAC protocol（理想 MAC 协议） gives full rate to one active node and equal share to multiple active nodes, is decentralized, and is simple.

### Channel Partitioning

- TDMA（Time Division Multiple Access，时分多址） divides time into slots.
- FDMA（Frequency Division Multiple Access，频分多址） divides frequency into bands.
- Partitioning avoids collisions but wastes capacity when assigned users are idle.

### Random Access

- Random access protocols transmit at full channel rate when a node has data.
- Collisions are allowed, then recovered using retransmission.
- Slotted ALOHA（时隙 ALOHA） requires time slots and frame synchronisation.
- Slotted ALOHA efficiency is `Np(1-p)^(N-1)` and approaches `1/e ≈ 0.37` at best.
- Pure ALOHA（纯 ALOHA） does not use slots and has maximum efficiency about `1/(2e) ≈ 0.18`.
- CSMA（Carrier Sense Multiple Access，载波侦听多路访问） listens before transmitting.
- CSMA can still have collisions because of propagation delay.
- CSMA/CD（碰撞检测） detects collisions, aborts transmission, and uses binary exponential backoff.
- CSMA/CA（碰撞避免） is used in WiFi because wireless collision detection is difficult.

### Taking-Turns Protocols

- Polling（轮询） has a master ask nodes to transmit.
- Token passing（令牌传递） allows only the node with the token to transmit.
- These avoid collisions but introduce control overhead and failure concerns.

### MAC Addresses and ARP

- MAC address（MAC 地址） is 48-bit link-layer address.
- MAC addresses are flat and portable.
- IP addresses are hierarchical and depend on network location.
- ARP（Address Resolution Protocol，地址解析协议） maps IP address to MAC address on the same LAN.
- ARP query is broadcast.
- ARP reply is usually unicast.
- ARP cache stores mappings temporarily.

### Ethernet

- Ethernet frame fields include preamble, destination MAC, source MAC, type, payload, and CRC.
- Ethernet is connectionless and unreliable at link layer; it does not use ACK/NAK.
- Shared Ethernet used CSMA/CD.
- Switched Ethernet gives each host a separate collision domain and usually full duplex.

### Switches

- Switches are link-layer store-and-forward devices.
- Switches are transparent（透明）: hosts do not need to know they exist.
- Switches are plug-and-play（即插即用） and self-learning（自学习）.
- Switch table entries include MAC address, interface, and timestamp.
- On receiving a frame, a switch learns the source MAC and incoming interface.
- If destination MAC is known on a different interface, the switch forwards there.
- If destination MAC is known on the same interface, the switch filters/drops it.
- If destination MAC is unknown, the switch floods it.

### Switches vs Routers

- Switches use MAC addresses and operate at link layer.
- Routers use IP addresses and operate at network layer.
- Switches self-learn tables; routers use routing algorithms/protocols.
- Both are store-and-forward devices.

### Exam Focus

- MAC addresses change hop-by-hop; IP source/destination stay end-to-end unless NAT is used.
- ARP works only within the same link/subnet.
- CRC detects errors; it does not correct them.
- Switch forwarding questions require checking destination known/unknown and incoming/outgoing interface.
- Ethernet switches eliminate collisions on full-duplex point-to-point links.

### Lecture Questions

Original question: Can Internet checksum, 2D parity, and CRC correct bit errors?

How to solve:
- Checksum and CRC detect but do not correct.
- 2D parity can correct single-bit errors.

Answer:
- Internet checksum: No. 2D parity: Yes. CRC: No.

Original question: What can a switch do?

How to solve:
- Switches learn, filter, forward, and extend LANs.

Answer:
- It can filter frames, forward frames, and extend a LAN.

Original question: As a packet moves over multiple links, what happens to source/destination MAC and IP addresses?

How to solve:
- IP addresses identify end hosts/interfaces at network layer.
- MAC addresses identify next-hop link-layer endpoints.

Answer:
- Source and destination MAC addresses change from link to link, while source and destination IP addresses remain the same.

Original question: When does a switch flood a frame?

How to solve:
- If destination MAC is not in the switch table, the switch does not know the output interface.

Answer:
- It floods the frame out all interfaces except the incoming interface.

## 10. Wireless and Mobility

### Wireless Network Elements

- Wireless hosts（无线主机） communicate over wireless links.
- Base station / Access Point, AP（基站/接入点） connects wireless hosts to the wired network.
- Infrastructure mode（基础设施模式） uses an AP.
- Ad hoc mode（自组织模式） has no AP; nodes organise and route themselves.
- Handoff（切换） happens when a mobile host changes AP/base station.

### Wireless Link Characteristics

- Path loss（路径损耗） reduces signal strength with distance.
- Interference（干扰） occurs when other transmissions use the same frequency.
- Multipath propagation（多径传播） causes reflected signals to arrive at different times.
- Signal-to-Noise Ratio, SNR（信噪比） affects bit error rate.
- Bit Error Rate, BER（误码率） decreases as SNR increases.
- Higher data rates usually require higher SNR for acceptable BER.
- Rate adaptation（速率自适应） changes modulation/coding rate based on channel quality.

### Hidden and Exposed Terminals

- Hidden terminal problem（隐藏终端问题）: two senders cannot hear each other but collide at a receiver.
- Example: A and C cannot hear each other, but both transmissions interfere at B.
- Exposed terminal problem（暴露终端问题）: a node unnecessarily defers because it hears a nearby transmission that would not interfere with its receiver.

### RTS/CTS

- RTS/CTS（Request To Send / Clear To Send，请求发送/允许发送） reserves the channel before data transmission.
- RTS/CTS sequence is RTS -> CTS -> DATA -> ACK.
- RTS/CTS helps hidden terminal scenarios because nearby nodes hearing CTS defer.
- RTS/CTS adds overhead, so it is mainly useful when collision cost is high.

### IEEE 802.11 WiFi

- IEEE 802.11 uses CSMA/CA（载波侦听多路访问/碰撞避免）.
- WiFi cannot reliably use CSMA/CD because a wireless sender cannot easily detect collisions while transmitting.
- Basic Service Set, BSS（基本服务集） consists of AP and associated wireless hosts.
- AP periodically sends beacon frames（信标帧） containing SSID and AP MAC address.
- Passive scanning（被动扫描） listens for beacons.
- Active scanning（主动扫描） sends probe requests and receives probe responses.
- Association（关联） connects a wireless host to an AP.
- After association, the host may use DHCP to obtain IP configuration.

### WiFi Frame Addressing

- 802.11 frames can contain up to four address fields.
- More than two addresses are needed because the AP bridges wireless and wired networks.
- In infrastructure mode, a frame may need receiver address, transmitter address, and final destination/source address.
- Example host-to-router via AP:
  receiver address is AP MAC,
  transmitter address is wireless host MAC,
  third address is router MAC.

### Exam Focus

- Hidden terminal is solved or reduced by RTS/CTS; exposed terminal is different and is about unnecessary silence.
- CSMA/CA is for WiFi; CSMA/CD is for classic wired Ethernet.
- SNR/BER/data rate tradeoff is central to wireless performance.
- Association and DHCP are different: association joins WiFi link; DHCP obtains IP configuration.
- WiFi address fields are often tested because AP forwarding needs extra addressing.

### Lecture Questions

Original question: What is the correct reservation process sequence?

How to solve:
- Sender first asks to transmit; receiver grants; data is sent; receiver ACKs.

Answer:
- RTS -> CTS -> DATA -> ACK.

Original question: Which multiple access technique is used by IEEE 802.11?

How to solve:
- WiFi avoids collisions rather than detecting them like wired Ethernet.

Answer:
- CSMA/CA.

Original question: Why is CSMA/CD not suitable for WiFi?

How to solve:
- Wireless sender's own signal is strong and collision detection at sender is unreliable.
- Hidden terminals can cause collision at receiver even if sender senses idle.

Answer:
- Because wireless devices cannot reliably detect collisions while transmitting and hidden terminals make carrier sensing incomplete.

## 10. Recap Checklist

### Weeks 1-3

- Internet architecture, network edge/core, packet switching, circuit switching.
- Delay components: processing, queueing, transmission, propagation.
- Traffic intensity and queueing.
- Throughput and bottleneck links.
- Application-layer protocol design.
- HTTP timing, persistent/non-persistent connections, pipelining, caching.
- SMTP and email transfer.
- DNS hierarchy, record types, iterative/recursive queries, caching.
- P2P and BitTorrent rarest-first/tit-for-tat.
- CDN redirection and replication.

### Weeks 4-5

- Transport multiplexing/demultiplexing.
- UDP header and checksum.
- Reliable data transfer protocols rdt1.0 to rdt3.0.
- Stop-and-wait utilisation.
- Pipelining, GBN, SR.
- TCP sequence/ACK numbers.
- TCP RTT estimation and timeout.
- TCP flow control.
- TCP connection setup and teardown.
- TCP congestion control, slow start, congestion avoidance, Tahoe/Reno.

### Weeks 7-8

- IP data plane and forwarding.
- IP header fields.
- Fragmentation and reassembly.
- IPv4 addressing, subnetting, CIDR, LPM.
- DHCP.
- NAT.
- ICMP.
- Link-state routing and Dijkstra.
- Distance-vector routing and Bellman-Ford.
- Count-to-infinity, split horizon, poison reverse.

### Weeks 9-10

- Error detection: parity, checksum, CRC.
- MAC protocols: TDMA, FDMA, ALOHA, CSMA, polling, token passing.
- Ethernet, CSMA/CD, binary exponential backoff.
- MAC addresses and ARP.
- Switch learning, filtering, forwarding, flooding.
- Wireless path loss, interference, multipath.
- SNR, BER, rate adaptation.
- Hidden/exposed terminals, RTS/CTS.
- 802.11 CSMA/CA, association, scanning, WiFi frame addresses.

## High-Yield Formula Sheet

- Transmission delay（发送时延）: `L / R`.
- Propagation delay（传播时延）: `d / s`.
- Traffic intensity（流量强度）: `rho = La / R`.
- Average throughput（平均吞吐量）: `delivered bits / transfer time`.
- Bottleneck throughput（瓶颈吞吐量）: `min(link rates)`.
- Non-persistent HTTP no parallelism: `2D + S0/C + N(2D + S/C)`.
- Persistent HTTP no pipelining: `2D + S0/C + N(D + S/C)`.
- Persistent HTTP with pipelining: `3D + S0/C + NS/C`.
- Stop-and-wait utilisation: `(L/R)/(RTT + L/R)`.
- SR maximum window with `k` bits: `2^(k-1)`.
- GBN sequence space condition: `2^k >= N + 1`.
- TCP EstimatedRTT: `(1-alpha)EstimatedRTT + alpha SampleRTT`.
- TCP DevRTT: `(1-beta)DevRTT + beta|SampleRTT - EstimatedRTT|`.
- TCP TimeoutInterval: `EstimatedRTT + 4DevRTT`.
- TCP approximate rate: `cwnd / RTT`.
- CIDR address count: `2^(32-prefix)`.
- Fragment offset unit: 8 bytes.
- Slotted ALOHA max efficiency: `1/e`.
- Pure ALOHA max efficiency: `1/(2e)`.

## High-Yield Exam Patterns

### Delay Calculation

Original problem type: packet size, link rate, RTT, and number of packets/objects are given.

Method:
- Convert bytes to bits.
- Compute transmission delay using `L/R`.
- Add RTTs only when the protocol requires waiting.
- Add queueing only when packets wait before transmission.

Common answer traps:
- Using bytes instead of bits.
- Confusing propagation delay with transmission delay.
- Multiplying RTTs by number of objects even when parallel connections or pipelining is used.

### DNS Record Type

Original problem type: DNS RR has given name and value fields.

Method:
- Hostname to IP means A.
- Domain to authoritative DNS hostname means NS.
- Alias to canonical hostname means CNAME.
- Domain to mail server hostname means MX.

Common answer traps:
- Choosing A whenever a DNS name appears in value.
- Forgetting MX is for email domain lookup.

### TCP Sequence/ACK Number

Original problem type: segment sequence number and payload length are given; compute ACK.

Method:
- Segment with seq `x` and payload length `L` carries bytes `x` to `x+L-1`.
- If all bytes are received in order, ACK is `x+L`.
- If an earlier byte is missing, ACK stays at the missing byte.

Common answer traps:
- Answering last byte received instead of next byte expected.
- Forgetting SYN and FIN each consume one sequence number.

### Subnetting

Original problem type: prefix and required subnets/hosts are given.

Method:
- Address count is `2^(32-prefix)`.
- Borrow enough bits for the required number of subnets.
- New prefix is old prefix plus borrowed bits.
- Usable host count is usually total minus 2.

Common answer traps:
- Confusing number of subnets with number of hosts.
- Forgetting that `/23` has 512 addresses, not 256.

### Fragmentation

Original problem type: datagram size and MTU are given.

Method:
- Subtract IP header from original datagram to get data size.
- Full-fragment payload is `MTU - IP header`.
- Ensure full-fragment data size is a multiple of 8.
- Offset is cumulative data bytes before this fragment divided by 8.
- MF is 1 except for the final fragment.

Common answer traps:
- Calculating offset in bytes instead of 8-byte blocks.
- Forgetting each fragment has its own IP header.

### Routing

Original problem type: topology and link costs are given.

Method:
- For link-state, run Dijkstra from the source.
- For distance-vector, apply Bellman-Ford using each neighbour as possible next hop.
- If a failure occurs, identify whether routing tables are recomputed or static.

Common answer traps:
- Assuming bandwidth is always the routing metric.
- Forgetting distance-vector can converge slowly due to count-to-infinity.

### MAC and Switching

Original problem type: Ethernet frame arrives at a switch with a source/destination MAC.

Method:
- Learn source MAC on incoming interface.
- If destination known on different interface, forward.
- If destination known on same interface, filter/drop.
- If destination unknown, flood.

Common answer traps:
- Treating switch as router.
- Changing IP addresses at every link.

### Wireless

Original problem type: hidden terminal, exposed terminal, or RTS/CTS sequence.

Method:
- Hidden terminal: senders cannot hear each other but collide at receiver.
- Exposed terminal: node hears a transmission and unnecessarily stays silent.
- RTS/CTS order is RTS, CTS, DATA, ACK.

Common answer traps:
- Mixing CSMA/CD with WiFi.
- Saying RTS/CTS removes all wireless collisions; it only reduces hidden-terminal collisions and adds overhead.
