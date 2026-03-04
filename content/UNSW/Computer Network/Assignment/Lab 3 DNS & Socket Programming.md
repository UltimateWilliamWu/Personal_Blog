## **Exercise 3: Digging into DNS (marked, include in the lab report, 5 Marks)**

>[!note] Answer & Screenshots
>![[Pasted image 20260303142602.png |1000]]
>
>### **Question 1.** What is the IP address of **[www.optus.com.au](http://www.optus.com.au/)** ? What type of DNS query is sent to get this answer?  
>
>The IPv4 addresses returned for [www.optus.com.au](http://www.optus.com.au) are 23.55.242.122, 23.55.242.146, and 23.55.242.152. The DNS query type is A (address record).
>
> ### **Question 2.** What is the canonical name for the webserver (i.e., **[www.optus.com.au](http://www.optus.com.au/)** )? Suggest a reason for having an alias for this server.
>
>The canonical name (CNAME chain) for [www.optus.com.au](http://www.optus.com.au) is:
> [www.optus.com.au](http://www.optus.com.au) → optus.com.au.edgekey.net → e189255.a.akamaiedge.net
> So the canonical (final) name that the A records apply to is e189255.a.akamaiedge.net.
> - Reason for using an alias: This allows optus.com.au to map the “www” hostname to a CDN (Akamai) hostname. Using a CNAME enables traffic to be directed to nearby edge servers and supports load balancing, performance optimisation, and easier failover without changing the public [www.optus.com.au](http://www.optus.com.au) name.
>
> 
> ### **Question 3.** What can you make of the rest of the response/what is it used for (i.e., the details available in the DNS response (cookies and other fields))?  
>
>The additional fields show that the response was provided by a recursive resolver (`rd` and `ra` flags), and that EDNS was used (OPT pseudo-section with UDP size). The DNS COOKIE option indicates extra security/anti-spoofing support. `Query time`, `SERVER`, and `MSG SIZE` provide performance and debugging information.
> 
> ### **Question 4.** What is the IP address of the local nameserver for your machine?
>
>The IP address of my machine’s local name server is **129.94.208.2**. This is shown on the `SERVER:` line in the `dig` output (`SERVER: 129.94.208.2#53`).
> 
> ### **Question 5.** What are the DNS nameservers for the " **netflix.com** ” domain (note: the domain name is **netflix.com.** and not **[www.netflix.com](http://www.netflix.com/)** . This is an example of what is referred to as the apex/naked domain)? Find their IP addresses. Which DNS query type is used to obtain this information?
>
>![[Pasted image 20260304223440.png|1000]]
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
> ![[Pasted image 20260304224126.png|1000]]
> The DNS name (reverse DNS / PTR record) associated with **9.9.9.9** is **dns9.quad9.net.**  
>The DNS query type used to obtain this information is **PTR** (a reverse lookup, e.g., `dig -x 9.9.9.9`).
> 
> ### **Question 7.** Run dig and query the CSE nameserver (129.94.242.2) for the mail servers for google.com (again, the domain name is google.com, not [www.google.com](http://www.google.com/) ). Did you get an authoritative answer? Why? (HINT: Just because a response contains information in the authoritative part of the DNS response message does not mean it came from an authoritative name server. You should examine the flags in the response message to determine the answer)
> 
> ![[Pasted image 20260304224256.png|1000]]
> I queried the CSE nameserver using `dig @129.94.242.2 google.com MX`. The reply was **not authoritative** because the **`aa` flag is not set** in the response (the flags are `qr rd ra`). This indicates that **129.94.242.2 is acting as a recursive resolver**, returning an answer obtained via recursion and/or cache, rather than being an authoritative nameserver for the `google.com` zone. The presence (or absence) of an AUTHORITY section alone does not prove authoritativeness; the **DNS flags** are the reliable indicator.
> 
> ### **Question 8.** Obtain the authoritative answer for the mail servers for google.com. What type of DNS query is sent to obtain this information?
> 
> ![[Pasted image 20260304224526.png|1000]]
> ![[Pasted image 20260304224644.png|1000]]
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
> 
> I compared DNS resolution performance for the **A record of `www.discord.com`** using the CSE DNS resolver and three public resolvers (Google Public DNS, Cloudflare DNS, OpenDNS). I queried each resolver once with `dig @<resolver> www.discord.com A` and recorded the reported **Query time**.
> 
> #### Resolution times
> 
> - **CSE DNS (129.94.242.2):** **7 ms**
>     
> - **Google Public DNS (8.8.8.8):** **7 ms**
>     
> - **Cloudflare DNS (1.1.1.1):** **3 ms**
>     
> - **OpenDNS (208.67.222.222):** **27 ms**
>     
> 
> #### Notable observations
> 
> 1. **Fastest resolver:** Cloudflare (**3 ms**) was the fastest in this measurement, suggesting lower latency from the test host to Cloudflare or a very warm cache for this query.
>     
> 2. **Slowest resolver:** OpenDNS (**27 ms**) was noticeably slower than the others (3–7 ms range). This could be due to higher network latency to OpenDNS from the test environment or different caching/anycast routing behaviour.
>     
> 3. **Caching / TTL:** All responses returned the same TTL for the A records (**300 seconds**), and the IP set was consistent across resolvers (five `162.159.x.x` addresses). The ordering differed slightly, which is normal (load balancing / round-robin ordering).
>     
> 4. **DNSSEC-related flags:** All replies included the **`ad`** flag (`flags: qr rd ra ad`), indicating the resolver returned authenticated data (DNSSEC validation performed by the resolver, depending on resolver policy).
>     
> 5. **EDNS / response size differences:**
>     
>     - CSE used EDNS UDP size **1232** and returned `MSG SIZE rcvd: 152` (it also included a COOKIE line).
>         
>     - Google’s EDNS UDP size was **512**, with `MSG SIZE rcvd: 124`.
>         
>     - Cloudflare used **1232**, `MSG SIZE rcvd: 124`.
>         
>     - OpenDNS used **1410**, `MSG SIZE rcvd: 124`.  
>         The response size variation (e.g., CSE’s larger size) is likely due to additional EDNS options such as cookies or resolver-specific metadata, not differences in the A-record content.
> 
> ### **Question 10.** In this exercise, you will simulate the iterative DNS query process to find the IP address of your machine (e.g., lyre00.cse.unsw.edu.au). If you are using VLAB, your hostname will begin with **vx** . Begin by finding the nameservers (query type **NS** ) for the **root (“.”) domain** . From the list of root nameservers in the response, choose one authoritative server and query it for the next step in the delegation chain. Use the **correct DNS query type** each time.Receiving a DNS response does **not** guarantee that the answer is correct or authoritative. Pay close attention to the **ANSWER** section and the **authority flags** in each response. Repeat this process by querying each successive authoritative nameserver until you eventually retrieve the **authoritative IP address** for the given hostname. **How many DNS servers did you have to query** before obtaining the final authoritative answer (the IP address of your lab machine)?



        

### Overall pattern

For this single measurement, **Cloudflare performed best**, **CSE and Google were similar**, and **OpenDNS was significantly slower**. All resolvers behaved as **recursive resolvers** (they all had `rd` and `ra` set) and returned consistent A-record data.
## Exercise 4: A Simple Web Server (Marked, submit your code, 5 Marks)
