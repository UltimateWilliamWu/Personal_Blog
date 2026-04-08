## Exercise 1: Understanding TCP using Wireshark (Marked, include in the lab report, 5 Marks)

>[!note] Answer & Screenshots
>#### **Question 1.** What is the IP address of gaia.cs.umass.edu? On what port number is it sending and receiving TCP segments for this connection? What are the IP address and TCP port numbers used by the client computer (source) that is transferring the file to gaia.cs.umass.edu?
>
>![[Pasted image 20260407153350.png|1000]]
>
>The IP address of gaia.cs.umass.edu is 128.119.245.12. It uses TCP port 80 for this connection. The client IP address is 192.168.1.102 and the client TCP port number is 1161.
>
>#### **Question 2.** What is the sequence number of the TCP segment containing the HTTP POST command? Note that to find the POST command, you'll need to dig into the packet content field at the bottom of the Wireshark window, looking for a segment with a "POST" within its DATA field.
>
>![[Pasted image 20260407154308.png|1000]]
>
>The sequence number of the TCP segment containing the HTTP POST command is 232129013.
>#### **Question 3.** Consider the TCP segment containing the HTTP POST as the first segment in the TCP connection.
> 
> (a) What are the sequence numbers of the first six segments in the TCP connection (including the segment containing the HTTP POST) sent from the client to the webserver (do not consider the ACKs received from the server as part of these six segments)?
>
>| Segment No. | Packet No. | Sequence Number |
| --- | --- | --- |
| 1 | 4 | 232129013 |
| 2 | 5 | 232129578 |
| 3 | 7 | 232131038 |
| 4 | 8 | 232132498 |
| 5 | 10 | 232133958 |
| 6 | 11 | 232135418 |
> (b) At what time was each segment sent? When was the ACK for each segment received? Given the difference between when each TCP segment was sent and when its acknowledgement was received, what is the RTT value for each of the six segments?
>
>| Segment No. | Packet No. | Send Time (s) | ACK Packet No. | ACK Time (s) | RTT (s) |
| --- | --- | --- | --- | --- | --- |
| 1 | 4 | 0.026477 | 6 | 0.053937 | 0.027460 |
| 2 | 5 | 0.041737 | 9 | 0.077294 | 0.035557 |
| 3 | 7 | 0.054026 | 12 | 0.124085 | 0.070059 |
| 4 | 8 | 0.054690 | 14 | 0.169118 | 0.114428 |
| 5 | 10 | 0.077405 | 15 | 0.217299 | 0.139894 |
| 6 | 11 | 0.078157 | 16 | 0.267802 | 0.189645 |
>The RTT for each segment is calculated as:
RTT = ACK arrival time - segment send time
Thus, the RTT values for the first six segments are:
0.027460 s, 0.035557 s, 0.070059 s, 0.114428 s, 0.139894 s, and 0.189645 s.
>
> (c) What is the _EstimatedRTT_ value (see relevant parts of Section 3.5 or lecture slides) after receiving each ACK? Assume that the initial value of _EstimatedRTT_ is equal to the measured RTT ( _SampleRTT_ ) for the first segment and then is computed using the _EstimatedRTT_ equation for all subsequent segments. Set alpha to 0.125.
>
>| Segment No. | SampleRTT (s) | EstimatedRTT (s) |
| --- | --- | --- |
| 1 | 0.027460 | 0.027460 |
| 2 | 0.035557 | 0.028472 |
| 3 | 0.070059 | 0.033670 |
| 4 | 0.114428 | 0.043765 |
| 5 | 0.139894 | 0.055781 |
| 6 | 0.189645 | 0.072514 |
>The initial EstimatedRTT is set equal to the SampleRTT of the first segment.
For each subsequent ACK, EstimatedRTT is calculated using:
EstimatedRTT = (1 - alpha) × Previous EstimatedRTT + alpha × SampleRTT
where alpha = 0.125.
Using this formula, the EstimatedRTT values after receiving the ACKs for the first six segments are:
0.027460 s, 0.028472 s, 0.033670 s, 0.043765 s, 0.055781 s, and 0.072514 s.
>
>(d) What is the length of each of the first six TCP segments?
>
>| Segment No. | Packet No. | TCP Segment Length (bytes) |
| --- | --- | --- |
| 1 | 4 | 565 |
| 2 | 5 | 1460 |
| 3 | 7 | 1460 |
| 4 | 8 | 1460 |
| 5 | 10 | 1460 |
| 6 | 11 | 1460 |
>The lengths of the first six TCP segments are 565 bytes, 1460 bytes, 1460 bytes, 1460 bytes, 1460 bytes, and 1460 bytes.
> #### **Question 4.** What is the minimum amount of available buffer space advertised at the receiver for the entire trace? Does the lack of receiver buffer space ever throttle the sender?
> The minimum amount of available buffer space advertised by the receiver over the entire trace is 5840 bytes. This value appears in the first ACK sent by gaia.cs.umass.edu. The advertised receive window then increases gradually during the connection.
>
No, the sender is not throttled by the lack of receiver buffer space in this trace. The receiver window never drops to zero or to a critically small value that would prevent the sender from continuing transmission.
> #### **Question 5.** Are there any retransmitted segments in the trace file? To answer this question, what did you check for (in the trace)?
> There are no retransmitted segments in the trace file.
>
To determine this, I checked the sequence numbers of the TCP segments sent from the client to the server and found that they increase monotonically over time. A retransmission would normally appear as a segment with a sequence number that had already been sent earlier. This can also be verified in the Time-Sequence-Graph (Stevens), where no backward jump or repeated sequence region is observed.
> #### **Question 6.** How much data does the receiver typically acknowledge in an ACK? Can you identify cases where the receiver is ACKing every other received segment (recall the discussion about delayed ACKs from the lecture notes or Section 3.5 of the text)?
> The receiver typically acknowledges 1460 bytes of data in each ACK, which corresponds to one full-sized TCP segment.
>
>Yes, there are cases where the receiver ACKs every other received segment. In those cases, the ACK number increases by 2920 bytes, which is 2 × 1460 bytes. This indicates delayed ACK behavior, where the receiver waits and cumulatively acknowledges two full-sized segments with a single ACK. For example, later in the trace there are ACKs such as packet 80 that acknowledge 2920 bytes.
>####  **Question 7.** What is the TCP connection's throughput (bytes transferred per unit of time during the connection)? Explain how you calculated this value.
>The TCP connection throughput is approximately 30222 bytes/second, or about 30.22 KBytes/sec.
>
I calculated this by dividing the total amount of transmitted data by the total transmission time over the connection. The total transmitted data is the difference between the sequence number of the first data segment and the acknowledgement number of the last ACK:
>
Total data = 164091 - 1 = 164090 bytes
>
The total transmission time is the difference between the time of the first data segment and the time of the last ACK:
>
Total time = 5.455830 - 0.026477 = 5.429353 seconds
>
Therefore:
>
Throughput = 164090 / 5.429353 ≈ 30222 bytes/second ≈ 30.22 KBytes/sec
## Exercise 2: TCP Connection Management (Marked, include in the lab report, 5 Marks)

>[!note] Answer
>#### **Question 1.** What is the sequence number of the TCP SYN segment that is used to initiate the TCP connection between the client computer and server?
>
>The sequence number of the TCP SYN segment that is used to initiate the TCP connection is **2818463618**. This is shown in packet **295**, which is sent from the client (**10.9.16.201**) to the server (**10.99.6.175**).
>
>#### **Question 2.** What is the sequence number of the SYNACK segment sent by the server to the client computer in reply to the SYN? What is the value of the Acknowledgement field in the SYNACK segment? How did the server determine that value?
>
>The SYNACK segment sent by the server in reply to the SYN is packet **296**.
>
>The sequence number of this SYNACK segment is **1247095790**.
>
>The acknowledgement number is **2818463619**.
>
>The server determined this acknowledgement number by taking the client's initial sequence number (**2818463618**) and adding **1**, because the TCP SYN flag consumes one sequence number.
>
>#### **Question 3.** What is the sequence number of the ACK segment sent by the client computer in response to the SYNACK? What is the value of the Acknowledgment field in this ACK segment? Does this segment contain any data?
>
>The ACK segment sent by the client in response to the SYNACK is packet **297**.
>
>The sequence number of this ACK segment is **2818463619**.
>
>The acknowledgement number is **1247095791**.
>
>The acknowledgement number is obtained by taking the server's SYN sequence number (**1247095790**) and adding **1**, since the server's SYN also consumes one sequence number.
>
>This segment does not contain any data. It is a pure ACK segment.
>
>#### **Question 4.** Who has done the active close? Is it the client or the server? How have you determined this? What type of closure has been performed? 3 Segment (FIN/FINACK/ACK), 4 Segment (FIN/ACK/FIN/ACK) or Simultaneous close?
>
>The client performs the active close, because the first FIN segment is sent by the client in packet **304**.
>
>The connection uses a simultaneous close.
>
>This can be determined from the packet sequence:
>
>- Packet **304**: client sends **FIN, ACK**
>- Packet **305**: server sends **FIN, ACK**
>- Packet **306**: client sends **ACK**
>- Packet **308**: server sends **ACK**
>
>A key observation is that in packet **305**, the server sends its own FIN before fully acknowledging the client's FIN. The ACK number in packet **305** is **2818463652**, whereas acknowledging the client's FIN would require **2818463653**. Therefore, both sides are attempting to close the connection at nearly the same time, which indicates a simultaneous close.
>
>#### **Question 5.** How many data bytes have been transferred from the client to the server and from the server to the client during the whole duration of the connection? What relationship does this have with the Initial Sequence Number and the final ACK received from the other side?
>
>The amount of data transferred from the client to the server is **33** bytes.
>
>This is obtained from the server's ACK in packet **301**:
>
>- First client data sequence number = **2818463619**
>- ACK from server = **2818463652**
>- Data bytes sent = **2818463652 - 2818463619 = 33 bytes**
>
>The amount of data transferred from the server to the client is **40** bytes.
>
>This is obtained from the client's ACK in packet **303**:
>
>- First server data sequence number = **1247095791**
>- ACK from client = **1247095831**
>- Data bytes sent = **1247095831 - 1247095791 = 40 bytes**
>
>The relationship with the Initial Sequence Number (ISN) and the final ACK is:
>
>**Final ACK = ISN + 1 + data bytes + 1**
>
>The first **+1** is because the SYN consumes one sequence number.
>
>The second **+1** is because the FIN consumes one sequence number.
>
>For the client side:
>
>- Final ACK from server = **2818463653**
>- Client ISN = **2818463618**
>- Data bytes = **2818463653 - 2818463618 - 2 = 33 bytes**
>
>For the server side:
>
>- Final ACK from client = **1247095832**
>- Server ISN = **1247095790**
>- Data bytes = **1247095832 - 1247095790 - 2 = 40 bytes**
>
>Therefore, the final ACK from the other side reflects the sender's ISN, all transmitted data bytes, and one sequence number consumed by each of the SYN and FIN flags.
