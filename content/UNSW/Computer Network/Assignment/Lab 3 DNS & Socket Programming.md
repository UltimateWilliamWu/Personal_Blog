---
tags:
  - UNSW
  - UNSW/COMP9331
  - Topic/Networking
  - Type/Lab
---

## **Exercise 3: Digging into DNS (marked, include in the lab report, 5 Marks)**

>[!note] Answer & Screenshots
>![[Pasted image 20260310110801.png|1000]]
>
>### **Question 1.** What is the IP address of **[www.optus.com.au](http://www.optus.com.au/)**? What type of DNS query is sent to get this answer?
>
>The IPv4 addresses returned for [www.optus.com.au](http://www.optus.com.au) are **23.48.247.241** and **23.48.247.242**.
>
>The DNS query type is **A** (address record).
>
>### **Question 2.** What is the canonical name for the webserver (i.e., **[www.optus.com.au](http://www.optus.com.au/)**)? Suggest a reason for having an alias for this server.
>
>The canonical name of **www.optus.com.au** is **e189255.a.akamaiedge.net**.
>
>From the **dig** output, **www.optus.com.au** is first mapped to **optus.com.au.edgekey.net**, which is then mapped to **e189255.a.akamaiedge.net** through CNAME records.
>
>A reason for using an alias is that it allows the website to use a CDN provider such as Akamai for better performance, load balancing, and reliability. It also makes it easier to change the underlying servers without changing the public hostname.
>
>### **Question 3.** What can you make of the rest of the response/what is it used for (i.e., the details available in the DNS response: cookies and other fields)?
>
>The additional fields show that the response was provided by a recursive resolver (**rd** and **ra** flags), and that EDNS was used (OPT pseudo-section with UDP size). The DNS COOKIE option indicates extra security and anti-spoofing support.
>
>**Query time**, **SERVER**, and **MSG SIZE** provide performance and debugging information.
>
>### **Question 4.** What is the IP address of the local nameserver for your machine?
>
>The IP address of my machine's local nameserver is **129.94.242.2**. This is shown on the **SERVER:** line in the **dig** output (**SERVER: 129.94.242.2#53**).
>
>### **Question 5.** What are the DNS nameservers for the **netflix.com** domain (note: the domain name is **netflix.com.** and not **[www.netflix.com](http://www.netflix.com/)**. This is an example of the apex/naked domain)? Find their IP addresses. Which DNS query type is used to obtain this information?
>
>![[Pasted image 20260310112153.png|1000]]
>
>The apex domain **netflix.com.** has the following DNS nameservers (from an **NS** query):
>
>- **ns-1984.awsdns-56.co.uk.**
>- **ns-659.awsdns-18.net.**
>- **ns-81.awsdns-10.com.**
>- **ns-1372.awsdns-43.org.**
>
>Their IPv4 addresses (from **A** queries) are:
>
>- **ns-1984.awsdns-56.co.uk.** -> **205.251.199.192**
>- **ns-659.awsdns-18.net.** -> **205.251.194.147**
>- **ns-81.awsdns-10.com.** -> **205.251.192.81**
>- **ns-1372.awsdns-43.org.** -> **205.251.197.92**
>
>**DNS query type used to obtain the nameserver list:** **NS**
>
>**DNS query type used to obtain the IP addresses:** **A** (for IPv4; **AAAA** would be used for IPv6 if needed)
>
>### **Question 6.** What is the DNS name associated with the IP address **9.9.9.9**? Which DNS query type is used to obtain this information?
>
>![[Pasted image 20260310112327.png|1000]]
>
>The DNS name (reverse DNS / PTR record) associated with **9.9.9.9** is **dns9.quad9.net.**
>
>The DNS query type used to obtain this information is **PTR** (a reverse lookup, e.g., **dig -x 9.9.9.9**).
>
>### **Question 7.** Run **dig** and query the CSE nameserver (**129.94.242.2**) for the mail servers for **google.com** (again, the domain name is **google.com**, not [www.google.com](http://www.google.com/)). Did you get an authoritative answer? Why?
>
>![[Pasted image 20260310112710.png|1000]]
>
>I queried the CSE nameserver using **dig @129.94.242.2 google.com MX**. The reply was **not authoritative** because the **aa** flag is not set in the response (**flags: qr rd ra**).
>
>This indicates that **129.94.242.2 is acting as a recursive resolver**, returning an answer obtained via recursion and/or cache, rather than being an authoritative nameserver for the **google.com** zone.
>
>The presence (or absence) of an AUTHORITY section alone does not prove authoritativeness; the **DNS flags** are the reliable indicator.
>
>### **Question 8.** Obtain the authoritative answer for the mail servers for **google.com**. What type of DNS query is sent to obtain this information?
>
>![[Pasted image 20260310112822.png|1000]]
>![[Pasted image 20260310113039.png|1000]]
>
>To obtain an authoritative answer for the mail servers of **google.com**, I queried one of Google's authoritative nameservers directly:
>
>**dig @ns1.google.com google.com MX**
>
>The reply is **authoritative** because the **aa** flag is set in the response (**flags: qr aa rd**). The MX record returned is:
>
>- **google.com. IN MX 10 smtp.google.com.**
>
>The DNS query type used to obtain the mail-server information is **MX**.
>
>### **Question 9.** Compare the performance of publicly available DNS resolvers for **www.discord.com** with the performance of the CSE DNS server. Select **three** publicly available DNS servers from the following list to query for type A record:
>
>- **Google Public DNS** **8.8.8.8**
>- **Cloudflare DNS** **1.1.1.1**
>- **OpenDNS** **208.67.222.222**
>- **NextDNS** **45.90.28.232**
>
>Measure and compare the DNS resolution times for each chosen resolver against the CSE DNS server. In your answer, include the resolution time for each server, notable differences (e.g., caching behavior, DNSSEC flags, response size), and any interesting patterns.
>
>![[Pasted image 20260310113644.png|1000]]
>![[Pasted image 20260310113710.png|1000]]
>![[Pasted image 20260310113735.png|1000]]
>![[Pasted image 20260310113759.png|1000]]
>
>| Resolver | Server IP | Query Time | TTL | Flags | Message Size | Notes |
>| --- | --- | ---: | ---: | --- | ---: | --- |
>| CSE DNS server | 129.94.242.2 | **3 ms** | 300 | **qr rd ra ad** | 152 bytes | Fastest overall |
>| Google Public DNS | 8.8.8.8 | **7 ms** | 300 | **qr rd ra ad** | 124 bytes | Fastest public resolver |
>| Cloudflare DNS | 1.1.1.1 | **7 ms** | 300 | **qr rd ra ad** | 124 bytes | Same query time as Google |
>| OpenDNS | 208.67.222.222 | **11 ms** | 300 | **qr rd ra ad** | 124 bytes | Slowest in this test |
>
>#### Comparison and observations
>
>Based on the measured query times, the **CSE DNS server** performed best at **3 ms**. **Google Public DNS** and **Cloudflare DNS** both took **7 ms**, and **OpenDNS** was the slowest at **11 ms**.
>
>All four resolvers returned the **same set of five A records** for **www.discord.com**, while the ordering of returned IP addresses varied slightly. This is normal load-distribution behavior.
>
>In this measurement round, the TTL values were **identical** across all four resolvers (**300**). This indicates each resolver returned records with the same remaining lifetime at that moment.
>
>DNS flags were identical in all cases: **qr rd ra ad**. This indicates recursion support and authenticated data in the replies.
>
>The CSE response size (**152 bytes**) was larger than the public resolvers (**124 bytes**), likely due to additional EDNS metadata (e.g., COOKIE information) in the OPT pseudo-section.
>
>Overall, the CSE DNS server was fastest in this measurement, likely due to network proximity. Public resolvers were close in performance but still slower in this run.
>
>### **Question 10.** **How many DNS servers did you have to query** before obtaining the final authoritative answer (the IP address of your lab machine)?
>
>![[Pasted image 20260310002504.png|1000]]
>![[Pasted image 20260310121631.png|1000]]
>![[Pasted image 20260310121755.png|1000]]
>![[Pasted image 20260310123520.png|1000]]
>![[Pasted image 20260310123648.png|1000]]
>![[Pasted image 20260310123748.png|1000]]
>
>To simulate the iterative DNS query process for **vx10.cse.unsw.edu.au**, I queried each hierarchy level using **dig +norecurse** and followed referrals until I reached the authoritative server.
>
>| Step | Server queried | Query | Result |
>| --- | --- | --- | --- |
>| 1 | Local resolver | **. NS** | Returned the list of root nameservers |
>| 2 | **a.root-servers.net** (**198.41.0.4**) | **au NS** | Returned delegation to **.au** nameservers |
>| 3 | **t.au** (**65.22.199.1**) | **edu.au NS** | Returned delegation to **edu.au** nameservers |
>| 4 | One **edu.au** authoritative nameserver | **unsw.edu.au NS** | Returned delegation to **ns1-ext.unsw.edu.au**, **ns2-ext.unsw.edu.au**, **ns3-ext.unsw.edu.au** |
>| 5 | **ns1-ext.unsw.edu.au** (**54.79.80.189**) | **cse.unsw.edu.au NS** | Returned delegation to **maestro.orchestra.cse.unsw.edu.au** and **beethoven.orchestra.cse.unsw.edu.au** |
>| 6 | **maestro.orchestra.cse.unsw.edu.au** (**129.94.242.33**) | **vx10.cse.unsw.edu.au A** | Returned authoritative IP **129.94.242.150** |
>
>### Final authoritative answer
>
>The authoritative IP address of **vx10.cse.unsw.edu.au** is:
>
>> **129.94.242.150**
>
>This answer is authoritative because the final response included the **aa** flag and the IP appeared in the **ANSWER SECTION**.
>
>### How many DNS servers were queried?
>
>I made **6 query steps** in total and contacted **5 unique DNS servers** (counting the local resolver once).
>
>Counting note: **including** the local resolver gives **5 unique servers**; **excluding** the local resolver gives **4 external DNS servers**.
>
>Unique servers:
>
>1. **Local resolver**
>2. **a.root-servers.net**
>3. **t.au**
>4. **ns1-ext.unsw.edu.au**
>5. **maestro.orchestra.cse.unsw.edu.au**

## Exercise 4: A Simple Web Server (Marked, submit your code, 5 Marks)

>[!note] Answer & Validation
>
>I implemented a custom HTTP server in **WebServer.py** using Python's low-level **socket** API (without using pre-made web server modules such as **http.server**).
>
>### Run command
>
>```bash
>python3 WebServer.py 55080
>```
>
>### Test results
>
>- Request: **http://127.0.0.1:55080/index.html**  
>  Result: **200 OK**, page content displayed.
>
>- Request: **http://127.0.0.1:55080/myimage.jpeg**  
>  Result: **200 OK**, image displayed.
>
>- Request: **http://127.0.0.1:55080/bio.html** (non-existent file)  
>  Result: **404 Not Found**.
>
>### How the implementation matches requirements (i)-(ix)
>
>1. **Create connection socket**: server creates TCP socket, binds to the given port, listens, and accepts browser connections.
>2. **Receive HTTP requests**: server reads requests from the accepted TCP connection; only **GET** is processed.
>3. **Parse requested file**: request line is parsed to get the target path (e.g., **/index.html**).
>4. **Read file from filesystem**: requested file is loaded from the server working directory.
>5. **Create HTTP response**: response includes status line + headers + file body.
>6. **Send response via TCP**: response is sent with **sendall()** on the same connection socket.
>7. **404 handling**: if file is missing, server sends **HTTP/1.1 404 Not Found** with an HTML error body.
>8. **Listen in loop**: server continuously accepts new client connections in a main loop.
>9. **HTTP/1.1 persistent connections**: the server handles multiple requests on the same TCP connection (keep-alive by default in HTTP/1.1, closed only when **Connection: close** is requested).
>
>### Extra behavior
>
>- For **/favicon.ico**, the server returns **204 No Content** (allowed by lab notes).
