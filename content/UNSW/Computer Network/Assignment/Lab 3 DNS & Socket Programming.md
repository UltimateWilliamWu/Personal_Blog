## **Exercise 3: Digging into DNS (marked, include in the lab report, 5 Marks)**

>[!note] Answer & Screenshots
>![[Pasted image 20260303142602.png]]
>
>**Question 1.** What is the IP address of **[www.optus.com.au](http://www.optus.com.au/)** ? What type of DNS query is sent to get this answer?  
>
>The IPv4 addresses returned for [www.optus.com.au](http://www.optus.com.au) are 23.55.242.122, 23.55.242.146, and 23.55.242.152. The DNS query type is A (address record).
>
> **Question 2.** What is the canonical name for the webserver (i.e., **[www.optus.com.au](http://www.optus.com.au/)** )? Suggest a reason for having an alias for this server.
>
>The canonical name (CNAME chain) for [www.optus.com.au](http://www.optus.com.au) is:
> [www.optus.com.au](http://www.optus.com.au) → optus.com.au.edgekey.net → e189255.a.akamaiedge.net
> So the canonical (final) name that the A records apply to is e189255.a.akamaiedge.net.
> - Reason for using an alias: This allows optus.com.au to map the “www” hostname to a CDN (Akamai) hostname. Using a CNAME enables traffic to be directed to nearby edge servers and supports load balancing, performance optimisation, and easier failover without changing the public [www.optus.com.au](http://www.optus.com.au) name.
>
> 
> **Question 3.** What can you make of the rest of the response/what is it used for (i.e., the details available in the DNS response (cookies and other fields))?  
>
>The additional fields show that the response was provided by a recursive resolver (`rd` and `ra` flags), and that EDNS was used (OPT pseudo-section with UDP size). The DNS COOKIE option indicates extra security/anti-spoofing support. `Query time`, `SERVER`, and `MSG SIZE` provide performance and debugging information.
> 
> **Question 4.** What is the IP address of the local nameserver for your machine?
> 
> **Question 5.** What are the DNS nameservers for the " **netflix.com** ” domain (note: the domain name is **netflix.com.** and not **[www.netflix.com](http://www.netflix.com/)** . This is an example of what is referred to as the apex/naked domain)? Find their IP addresses. Which DNS query type is used to obtain this information?
> 
> **Question 6** . What is the DNS name associated with the IP address 9.9.9.9? Which DNS query type is used to obtain this information?
> 
> **Question 7.** Run dig and query the CSE nameserver (129.94.242.2) for the mail servers for google.com (again, the domain name is google.com, not [www.google.com](http://www.google.com/) ). Did you get an authoritative answer? Why? (HINT: Just because a response contains information in the authoritative part of the DNS response message does not mean it came from an authoritative name server. You should examine the flags in the response message to determine the answer)
> 
> **Question 8.** Obtain the authoritative answer for the mail servers for google.com. What type of DNS query is sent to obtain this information?
> 
> **Question 9:** Compare the performance of publicly available DNS resolvers for **www.discord.com** with the performance of the CSE DNS server. Select **three** publicly available DNS servers from the following list to query for type A record:
> 
> - **Google Public DNS** 8.8.8.8
> - **Cloudflare DNS** 1.1.1.1
> - **OpenDNS** 208.67.222.222
> - **NextDNS** 45.90.28.232
> 
> Measure and compare the DNS resolution times for each chosen resolver against the CSE DNS server. In your answer, include the resolution time for each server. Any notable differences you observe (e.g., caching behaviour, DNSSEC flags, response size, etc.). Discuss any interesting patterns or variations in performance across the resolve.
> 
> **Question 10.** In this exercise, you will simulate the iterative DNS query process to find the IP address of your machine (e.g., lyre00.cse.unsw.edu.au). If you are using VLAB, your hostname will begin with **vx** . Begin by finding the nameservers (query type **NS** ) for the **root (“.”) domain** . From the list of root nameservers in the response, choose one authoritative server and query it for the next step in the delegation chain. Use the **correct DNS query type** each time.Receiving a DNS response does **not** guarantee that the answer is correct or authoritative. Pay close attention to the **ANSWER** section and the **authority flags** in each response. Repeat this process by querying each successive authoritative nameserver until you eventually retrieve the **authoritative IP address** for the given hostname. **How many DNS servers did you have to query** before obtaining the final authoritative answer (the IP address of your lab machine)?

## Exercise 4: A Simple Web Server (Marked, submit your code, 5 Marks)
