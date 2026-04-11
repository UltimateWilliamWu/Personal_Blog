---
aliases:
  - Lab 5 TCP Congestion Control/IP Layer Routing
---

## Exercise 1: TCP Congestion Control Analysis (Marked, include in the lab report, 3 Marks)

>[!note] Answer & Screenshots
>### **Question 1.** Generate the Throughput graph for each flow. Why does throughput fluctuate? At what times does throughput drop to near-zero?
>
>**Throughput Graph for Flow 1 (10.0.0.1:49153 -> 10.0.0.2:8080)**
>
>![[Pasted image 20260411175130.png|1000]]
>
>**Throughput Graph for Flow 2 (10.0.0.2:49153 -> 10.0.0.1:8081)**
>
>![[Pasted image 20260411175250.png|1000]]
>
>The throughput fluctuates because the two bidirectional TCP flows compete for the same **1 Mbps bottleneck link** while each OnOff application tries to send at **900 kbps**. Since the total offered load exceeds the link capacity, the queue gradually fills up, packets are dropped when the queue overflows, and TCP congestion control reduces the sending rate. After the sender recovers and increases its congestion window again, throughput rises. This creates the repeated oscillating pattern visible in both graphs.
>
>The most obvious drop to near-zero occurs at around **3 seconds** in both flows. After that, throughput continues to fluctuate periodically, but most later drops are to a lower non-zero level rather than all the way to zero.
>
>### **Question 2.** Generate the RTT Graph for each flow. What is the typical RTT? Identify timestamps where RTT spikes and explain what causes them. How do RTT spikes correlate with throughput drops?
>
>**RTT Graph for Flow 1 (10.0.0.1:49153 -> 10.0.0.2:8080)**
>
>![[Pasted image 20260411175739.png|1000]]
>
>**RTT Graph for Flow 2 (10.0.0.2:49153 -> 10.0.0.1:8081)**
>
>![[Pasted image 20260411175900.png|1000]]
>
>For the flow **10.0.0.1:49153 -> 10.0.0.2:8080**, the RTT is typically around **210 ms to 280 ms**, with occasional spikes to about **300 ms to 410 ms**.
>
>For the flow **10.0.0.2:49153 -> 10.0.0.1:8081**, the RTT is typically lower, mostly around **0 ms to 70 ms**, with spikes up to about **95 ms to 200 ms**.
>
>The RTT spikes occur when packets build up in the queue on the bottleneck link. As the queue length increases, packets spend more time waiting before transmission, which raises the measured RTT. Typical spike periods are visible around **3 s**, **11 s**, **18 s**, and **24.5 to 25 s**.
>
>These RTT spikes correlate with the throughput drops because both are caused by congestion. As the queue fills, RTT rises first due to queueing delay. Once the queue overflows and packets are dropped, TCP reduces its sending rate, causing throughput to fall.
>
>### **Question 3.** Use tcp.analysis.retransmission to find retransmissions. Find at least 3 instances of packet loss. For each, identify what triggered the loss (timeout or duplicate ACK), how TCP responded, and the recovery time.
>
>The following three packet loss events were identified using the Wireshark filter:
>
>`tcp.analysis.retransmission || tcp.analysis.fast_retransmission`
>
>| Event | Packet No. | Time (s) | Flow | Trigger | TCP Response | Recovery Time (s) |
>| --- | --- | --- | --- | --- | --- | --- |
>| 1 | 331 | 1.373882 | 49153 -> 8080 | Duplicate ACKs | Wireshark marks this as **TCP Fast Retransmission**, indicating that TCP retransmitted the missing segment after receiving multiple duplicate ACKs rather than waiting for a timeout. | 0.897984 |
>| 2 | 379 | 1.482314 | 49153 -> 8081 | Duplicate ACKs | Wireshark marks this as **TCP Fast Retransmission**, indicating duplicate ACK based loss detection and immediate retransmission. | 0.688928 |
>| 3 | 458 | 1.655242 | 49153 -> 8080 | Duplicate ACKs | Wireshark marks this as **TCP Fast Retransmission**, again showing that TCP used duplicate ACKs to detect loss and retransmit early. | 0.825488 |
>
>For all three events, the loss was triggered by **duplicate ACKs**, not by a timeout, because Wireshark explicitly labels them as **TCP Fast Retransmission**. In each case, TCP responded by retransmitting the missing segment immediately and then continuing transmission once a later cumulative ACK confirmed that the lost data had been successfully received.

## Exercise 2: Implementing an NS3 Simulation (Marked, include in the lab report, 4.5 Marks)

>[!note] Answer & Screenshots
>### **Question 1.** Fill in all stubs, run the simulation, and produce a working NetAnim animation matching the topology above.
>
>The stubs in **exercise2.py** were completed by implementing the full **8-node topology**, configuring all **four TCP flows**, enabling **PCAP capture** on the bottleneck links, and setting fixed node positions for **NetAnim**. The simulation ran successfully and generated the expected output files, including **exercise2.xml** and the bottleneck PCAP traces.
>
>**NetAnim Screenshot**
>
>![[Pasted image 20260411190902.png|1000]]
>
>The NetAnim visualisation matches the required topology. The top row contains nodes **0-1-2-3**, the bottom row contains nodes **7-6-4-5**, and the vertical links connect node **2** to **4** and node **1** to **6** as specified. The packet arrows visible in the animation confirm that the TCP flows are active during the simulation.
