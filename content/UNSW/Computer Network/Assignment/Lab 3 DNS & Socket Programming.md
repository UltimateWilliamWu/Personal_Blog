## **Exercise 3: Digging into DNS (marked, include in the lab report, 5 Marks)**

>[!note] Answer & Screenshots
>![[Pasted image 20260310110801.png|1000]]
>
>### **Question 1.** What is the IP address of **[www.optus.com.au](http://www.optus.com.au/)** ? What type of DNS query is sent to get this answer?  
>
>The IPv4 addresses returned for [www.optus.com.au](http://www.optus.com.au) are **23.48.247.241** and **23.48.247.242**. The DNS query type is A (address record).
>
> ### **Question 2.** What is the canonical name for the webserver (i.e., **[www.optus.com.au](http://www.optus.com.au/)** )? Suggest a reason for having an alias for this server.
>
>The canonical name of `www.optus.com.au` is **e189255.a.akamaiedge.net**.  
>From the `dig` output, `www.optus.com.au` is first mapped to `optus.com.au.edgekey.net`, which is then mapped to `e189255.a.akamaiedge.net` through CNAME records.  
>
>A reason for using an alias is that it allows the website to use a CDN provider such as Akamai for better performance, load balancing, and reliability. It also makes it easier to change the underlying servers without changing the public hostname.
>
> 
> ### **Question 3.** What can you make of the rest of the response/what is it used for (i.e., the details available in the DNS response (cookies and other fields))?  
>
>The additional fields show that the response was provided by a recursive resolver (`rd` and `ra` flags), and that EDNS was used (OPT pseudo-section with UDP size). The DNS COOKIE option indicates extra security/anti-spoofing support. `Query time`, `SERVER`, and `MSG SIZE` provide performance and debugging information.
> 
> ### **Question 4.** What is the IP address of the local nameserver for your machine?
>
>The IP address of my machine’s local name server is **129.94.208.2**. This is shown on the `SERVER:` line in the `dig` output (`SERVER: 129.94.242.2#53`).
> 
> ### **Question 5.** What are the DNS nameservers for the " **netflix.com** ” domain (note: the domain name is **netflix.com.** and not **[www.netflix.com](http://www.netflix.com/)** . This is an example of what is referred to as the apex/naked domain)? Find their IP addresses. Which DNS query type is used to obtain this information?
>
>![[Pasted image 20260310112153.png|1000]]
The apex domain **netflix.com.** has the following DNS nameservers (from an **NS** query):
> 
> - **ns-1984.awsdns-56.co.uk.**
>     
> - **ns-659.awsdns-18.net.**
>     
> - **ns-81.awsdns-10.com.**
>     
> - **ns-1372.awsdns-43.org.**
>     
> 
> Their IPv4 addresses (from **A** queries) are:
> 
> - **ns-1984.awsdns-56.co.uk.** → **205.251.199.192**
>     
> - **ns-659.awsdns-18.net.** → **205.251.194.147**
>     
> - **ns-81.awsdns-10.com.** → **205.251.192.81**
>     
> - **ns-1372.awsdns-43.org.** → **205.251.197.92**
>     
> 
> **DNS query type used to obtain the nameserver list:** **NS**  
> **DNS query type used to obtain the IP addresses:** **A** (for IPv4; **AAAA** would be used for IPv6 if needed)
> 
> ### **Question 6** . What is the DNS name associated with the IP address 9.9.9.9? Which DNS query type is used to obtain this information?
> 
> ![[Pasted image 20260310112327.png|1000]]
> The DNS name (reverse DNS / PTR record) associated with **9.9.9.9** is **dns9.quad9.net.**  
>The DNS query type used to obtain this information is **PTR** (a reverse lookup, e.g., `dig -x 9.9.9.9`).
> 
> ### **Question 7.** Run dig and query the CSE nameserver (129.94.242.2) for the mail servers for google.com (again, the domain name is google.com, not [www.google.com](http://www.google.com/) ). Did you get an authoritative answer? Why? (HINT: Just because a response contains information in the authoritative part of the DNS response message does not mean it came from an authoritative name server. You should examine the flags in the response message to determine the answer)
> 
> ![[Pasted image 20260310112710.png|1000]]
> I queried the CSE nameserver using `dig @129.94.242.2 google.com MX`. The reply was **not authoritative** because the **`aa` flag is not set** in the response (the flags are `qr rd ra`). This indicates that **129.94.242.2 is acting as a recursive resolver**, returning an answer obtained via recursion and/or cache, rather than being an authoritative nameserver for the `google.com` zone. The presence (or absence) of an AUTHORITY section alone does not prove authoritativeness; the **DNS flags** are the reliable indicator.
> 
> ### **Question 8.** Obtain the authoritative answer for the mail servers for google.com. What type of DNS query is sent to obtain this information?
> 
> ![[Pasted image 20260310112822.png|1000]]
> ![[Pasted image 20260310113039.png|1000]]
> To obtain an authoritative answer for the mail servers of **google.com**, I queried one of Google’s authoritative nameservers directly:
> `dig @ns1.google.com google.com MX`
> 
> The reply is **authoritative** because the **`aa`** flag is set in the response (`flags: qr aa rd`). The MX record returned is:
> 
> - **google.com. IN MX 10 smtp.google.com.**
> 
> The DNS query type used to obtain the mail-server information is **MX**.
> 
> ### **Question 9:** Compare the performance of publicly available DNS resolvers for **www.discord.com** with the performance of the CSE DNS server. Select **three** publicly available DNS servers from the following list to query for type A record:
> 
> - **Google Public DNS** 8.8.8.8
> - **Cloudflare DNS** 1.1.1.1
> - **OpenDNS** 208.67.222.222
> - **NextDNS** 45.90.28.232
> 
> Measure and compare the DNS resolution times for each chosen resolver against the CSE DNS server. In your answer, include the resolution time for each server. Any notable differences you observe (e.g., caching behaviour, DNSSEC flags, response size, etc.). Discuss any interesting patterns or variations in performance across the resolve.
> ![[Pasted image 20260310113644.png]]
> ![[Pasted image 20260310113710.png]]
> ![[Pasted image 20260310113735.png]]
> ![[Pasted image 20260310113759.png]]
> 
| Resolver          | Server IP      | Query Time | TTL | Flags         | Message Size | Notes                          |
| ----------------- | -------------- | ---------: | --: | ------------- | -----------: | ------------------------------ |
| CSE DNS server    | 129.94.242.2   |   **3 ms** | 190 | `qr rd ra ad` |    152 bytes | Fastest                        |
| Google Public DNS | 8.8.8.8        |   **7 ms** | 300 | `qr rd ra ad` |    124 bytes | Slower than CSE and Cloudflare |
| Cloudflare DNS    | 1.1.1.1        |   **7 ms** | 248 | `qr rd ra ad` |    124 bytes | Fastest public resolver        |
| OpenDNS           | 208.67.222.222 |   **11 ms** | 300 | `qr rd ra ad` |    124 bytes | Same query time as Google      |
>
>
> ### **Question 10.** **How many DNS servers did you have to query** before obtaining the final authoritative answer (the IP address of your lab machine)?
> ![[Pasted image 20260310002504.png]]
> 


## Exercise 4: A Simple Web Server (Marked, submit your code, 5 Marks)

