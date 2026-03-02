---
tags:
  - Assignment
---
**ZID**: z5518601
**Name**: Tianxiong Wu
## **Exercise 2: Use ping to test host reachability (2 marks. 0.2 per each host)**
Are the following hosts reachable from your machine by using ping:
- [www.google.co.uk](http://www.google.co.uk/)
- [www.utoronto.ca](http://www.utoronto.ca/)
- www.cloudflare.com
- [ec.ho](http://ec.ho/)
- [west.cn](http://west.cn/)
- [defence.gov.au](http://defence.gov.au/)
- [yes.no](http://yes.no/)
- [one.one.one.one](http://one.one.one.one/)
- [theguardian.com](http://theguardian.com/)
- [xn--i-7iq.ws](http://xn--i-7iq.ws/)
If you observe that some hosts are unreachable, can you explain why? Check if the addresses unreachable by the ping command are reachable from the Web browser.
>[!note] Answer & Screenshots
>![[Pasted image 20260224195701.png]]
>![[Pasted image 20260224200156.png]]
>![[Pasted image 20260224200219.png]]
>![[Pasted image 20260224200259.png]]
>![[Pasted image 20260224200643.png]]
>![[Pasted image 20260224200732.png]]
>![[Pasted image 20260224200813.png]]
>![[Pasted image 20260224200854.png]]
>![[Pasted image 20260224200945.png]]
>![[Pasted image 20260224201018.png]]
From my tests, these three hosts were **unreachable or only partially reachable via ping**:
> - **ec.ho**: `ping` failed with _“Name or service not known”_, which indicates a **DNS resolution error** (the hostname could not be resolved to an IP address). The site was **also not reachable in a web browser**, which is consistent with a DNS/domain issue rather than ICMP filtering.
> - **west.cn**: `ping` showed **partial reachability** (some replies received but with packet loss). However, the website was **reachable in a web browser**. This suggests that **ICMP traffic may be rate-limited or filtered** somewhere along the path, while **HTTP/HTTPS (TCP 80/443)** remains allowed.
> - **defence.gov.au**: `ping` resulted in **100% packet loss**, but the website was **reachable in a web browser**. This strongly suggests that **ICMP Echo Requests/Replies are blocked by a firewall or security policy**, while web traffic over **HTTPS** is permitted.
> 
> **Overall conclusion:** `ping` tests **ICMP reachability**, which can be blocked or limited by firewalls even when the website is accessible via a browser. In contrast, the `ec.ho` result points to a **DNS/domain problem**, since both ping and browser access failed.
## **Exercise 3: Use traceroute to understand the network topology (4 marks)**
_Note: Include all traceroute outputs in your report._
1. Run traceroute (s) on your machine to uni-heidelberg.de **(NOT www.uni-heidelberg.de)** **.** You might have slightly different outputs, and your tutor will explain why.  

>[!note] Answer & Screenshots
>![[Pasted image 20260224202351.png]]
> #### 1.1 How many routers are there between your workstation and uni-heidelberg.de?
> My traceroute output shows hops **1 to 17**. In the captured output, the last visible hop is already inside the **University of Heidelberg** network (`...uni-heidelberg.de`).  
> So, based on what is shown:
> - The path contains **17 hops/routers** up to the last router displayed (hop 17).
> - This indicates **17 routers on the path before reaching the destination host** (or at least before the destination host reply appears — the destination line is not visible in the screenshot).
> #### 1.2 Identify the routers which are part of the UNSW network?
> These hops are clearly within UNSW are **hops 1 through 5**(based on `unsw.edu.au`, UNSW IP ranges, and private RFC1918 addressing):
> - **Hop 1:** `vlan380.cse.unsw.EDU.AU (129.94.208.1)` → UNSW (CSE VLAN gateway)
> - **Hop 2:** `129.94.39.17` → UNSW (129.94.0.0/16 is UNSW)
> - **Hops 3, 4, & 5 (Internal Network):** These hops primarily show IP addresses starting with `172.17.x.x`. These are private IP addresses, meaning they are used internally within an organization's local network. Because they appear right before the traffic hands off to the external internet provider, they represent UNSW's internal routing infrastructure.
> - **Hop 6 (The ISP):** At hop 6, you can see the domain `aarnet.net.au`. AARNet (Australia's Academic and Research Network) is the Internet Service Provider for Australian universities. Once the trace hits AARNet, your packets have officially left the UNSW campus network and are traveling across the broader internet backbone.
> #### 2. Which router is the first router outside of Australia?
> The first hop that is clearly outside Australia is:
> - **Hop 10/11:** `...bdr1.sing.sin.aarnet.net.au (113.197.15.231)`  
>     The hostname contains **`sing.sin`**, which strongly indicates **Singapore**.
> This is also supported by RTT behavior:
> - RTT is ~**46 ms** around hop 9–10 (Australia backbone)
> - RTT jumps to ~**92 ms** at the Singapore AARNet router (hop 10/11), consistent with an international link.
> So the **first router outside Australia is the AARNet Singapore router** (113.197.15.231).
> #### 3. Try to identify the approximate locations of the routers.
> ![[Pasted image 20260224211514.png]]
> The traceroute results reveal a long-distance terrestrial and transoceanic path. The journey begins in **Sydney (UNSW)**, moving westward across Australia to **Adelaide** and **Perth**. From Perth, the packet transitions to a subsea cable reaching **Singapore**, evidenced by the RTT increasing from ~46ms to ~92ms. A significant latency jump occurs between Singapore and **Amsterdam** (from 92ms to 296ms), representing the intercontinental transit to Europe. Finally, the path concludes in Germany, passing through **Frankfurt** before reaching the destination in **Heidelberg**.
>
|**Hop**|**Hostname / IP**|**Identified Acronym**|**Physical Location**|**Rationale / Clues**|
|---|---|---|---|---|
|**1-5**|`cse.unsw.EDU.AU`|**UNSW**|**Sydney, Australia**|The source node is located within the University of New South Wales campus network.|
|**6-8**|`nsw.aarnet.net.au`|**NSW**|**Sydney, Australia**|AARNet (Australia's Academic and Research Network) nodes in New South Wales.|
|**9**|`sa.aarnet / wa.aarnet`|**SA / WA**|**Adelaide / Perth**|Indicates the packet is traversing the Australian continent from South Australia (SA) to Western Australia (WA).|
|**10-11**|`sing.sin.aarnet.net.au`|**SIN / SING**|**Singapore**|Standard airport code for Singapore; a major subsea cable landing station for traffic leaving Australia.|
|**12-13**|`ams.nl.geant.net`|**AMS / NL**|**Amsterdam, Netherlands**|"AMS" refers to Amsterdam; "NL" is the country code for the Netherlands. GÉANT is the European pan-European data network.|
|**14**|`fra.de.geant.net`|**FRA / DE**|**Frankfurt, Germany**|"FRA" refers to Frankfurt, the primary internet hub in Germany ("DE").|
|**15-16**|`x-win.dfn.de`|**DFN / DE**|**Karlsruhe, Germany**|DFN is the German National Research and Education Network. "fzk" likely refers to the Forschungszentrum Karlsruhe.|
|**17-18**|`uni-heidelberg.de`|**Heidelberg**|**Heidelberg, Germany**|The final destination at the University of Heidelberg.|

2. Run a traceroute from your machine to the following destinations: (i) [www.nyu.edu](http://www.nyu.edu/) (ii) [www.aut.ac.nz](http://www.aut.ac.nz/) and (iii) [www.nottingham.ac.uk](http://www.nottingham.ac.uk/)

>[!note] Answer & Screenshots
>#### 1. Last common router (where the three paths diverge)
> 
> The **last hop that is common to all three destinations is hop 2**:
> 
> - **Hop 2:** `129.94.39.17`
> 
> After that they diverge:
> 
> - **NYU** goes to `172.17.47.11` at hop 3
> - **AUT** goes to `172.17.47.11` at hop 3
> - **Nottingham** goes to `172.17.47.2` at hop 3 (different)
>     
> So the **paths diverge at hop 3**, meaning **hop 2 is the last router they have in common**.
> ![[Pasted image 20260301213141.png]]
> ![[Pasted image 20260301213002.png]]
> ![[Pasted image 20260301213104.png]]
> #### 2. Is hop count proportional to physical distance?
> **No, not necessarily.** Hop count depends on routing policy (BGP), peering, MPLS, filtering, and how many layer-3 hops reply to TTL-expired probes—not just geography.

3. Several servers are distributed worldwide to provide a web interface from which you can perform a traceroute to any other host on the Internet. Here are two examples: (i) [http://lg.nexlinx.net.pk/](http://lg.nexlinx.net.pk/) and (ii) [www.as13030.net/traceroute.php](http://www.as13030.net/traceroute.php) .

>[!note] Answer & Screenshots
>![[Pasted image 20260224214217.png|800]]
>
>![[Pasted image 20260224214250.png|800]]
>#### 1. What are the IP addresses of the two servers that you have chosen?
>The IP addresses of the two looking-glass servers are **202.59.80.52 (lg.nexlinx.net.pk)** and **213.144.137.198 (as13030.net)**, as shown in the first line of my traceroute outputs.
>#### 2. Does the reverse path go through the same routers as the forward path?
>![[Pasted image 20260224220336.png|1000]]
>![[Pasted image 20260224220904.png|1000]]
>The reverse path does **not** traverse exactly the same set of routers as the forward path. This is expected due to **asymmetric routing** on the Internet, where BGP policies and peering arrangements may select different routes in each direction.
>#### 3. If you observe common routers between the forward and the reverse path, do you also observe the same IP addresses? Why or why not?
>No, some parts of the forward and reverse paths traverse common networks (e.g., Zayo `64.125.*` and AARNet `113.197.15.*`). However, even when a router is “common”, the **observed IP address may not be identical**. Traceroute shows the IP address of the interface that sends the ICMP reply, and routers have multiple interfaces; different interfaces may be used in each direction. In addition, ECMP load balancing, ICMP rate-limiting, and MPLS tunneling can cause some hops to appear as `* * *` or appear with different IPs across runs.

## **Exercise 4: Use ping to gain insights into network performance (4 marks)**
>[!note] Answer & Screenshots
>1. For each location, ﬁnd the (approximate) physical distance from UNSW . You can use a site like [Distance Calculator](https://www.distancecalculator.net/) , [Google Maps](https://www.google.com/maps) , or whatever you prefer to take this measurement. Then, compute the shortest possible time T for a packet from UNSW to reach that location. You should assume that the packet moves (i.e. propagates) at the speed of light, 3 x 10^8 m/s. Note that the shortest possible time will be the distance divided by the propagation speed.
>$$
>T=D/C,c=3\times10^8m/s 
>$$
>
| Location   | Distance(km) | T(ms) | RTT(ms) | Actual RTT(ms) | Ratio |
| ---------- | ------------ | ----- | ------- | -------------- |-------|
| NewYork    | 15594.27     | 51.98 | 103.96  | 247.14         | 4.75 |
| NewZealand | 2157.17      | 7.19  | 14.38   | 34.89          | 4.85 |
| Nottingham | 16974.84     | 56.58 | 113.16  | 261.76         | 4.63 |
>
> 2. Plot a graph where the x-axis represents the distance to each city (i.e. **New York, USA** , **Auckland, New Zealand** and **Nottingham, UK** ). The y-axis represents the ratio between the minimum delay (i.e. RTT) measured by the ping program (select the values for 50-byte packets) and the shortest possible time T to reach that city from UNSW. (Note that the y-values are no smaller than 2 since it takes at least 2*T time for any packet to reach the destination from UNSW and return).You can also use the provided [generate_plot.py](https://webcms3.cse.unsw.edu.au/COMP3331/26T1/resources/118373) to generate the plot. Download (to Vlab or personal machines with Python 3 installed). Open the [generate_plot.py](https://webcms3.cse.unsw.edu.au/COMP3331/26T1/resources/118373) and uncomment the designated lists, and replace them with the actual values.Can you think of at least two reasons why the y-axis values you plot are greater than 2?
> 
> ![[Figure_1.png]]
> 
> The plotted ratios are greater than 2 because the RTT is not purely the propagation delay. 
> - First, packets propagate mostly in optical fibre where the speed is significantly lower than $3\times10^8 m/s$ (vacuum), so the physical lower bound is underestimated. 
> - Second, Internet routing rarely follows the shortest geographic path: BGP policies and submarine cable topology often lead to longer routes than the great-circle distance. 
> - In addition, even the minimum RTT includes processing, transmission and (non-zero) queuing delays at routers and links.
> 
> #### 3. Is the delay to the destinations constant, or does it vary over time? Explain why.
> 
> The delay is **not constant**; it **varies over time**.
> Even when the physical path length (propagation delay) is essentially fixed, the measured RTT changes because:
> 
> - **Queuing delay fluctuates** as traffic load on links and routers changes (congestion comes and goes), which is usually the main source of short-term variation.
>     
> - **Routing and load balancing** (e.g., ECMP) can cause packets to take slightly different paths with different latencies.
>     
> - Routers and firewalls may **rate-limit or deprioritise ICMP** (ping) responses, introducing additional variability.
>     
> 
> 
>####  4. The measured delay (i.e., the delay you can see in the graphs) comprises propagation, transmission, processing, and queuing delays. Which of these delays depend on the packet size and which do not?
> - **Propagation delay**: **does not depend** on packet size. It is determined by the physical path length and the propagation speed of the medium.
>     
> - **Processing delay**: **does not depend** (or only very weakly depends) on packet size. It is mainly the time routers/switches spend examining headers and making forwarding decisions.
>     
> - **Transmission delay**: **depends directly** on packet size. It is the time to push L bits onto a link of rate R:
>     
>     $$d_{tx} = \frac{L}{R}$$​
>     
>     so larger packets take longer to transmit.
>     
> - **Queuing delay**: **not a fixed function** of packet size, but it can **increase with larger packets**, especially under load, because larger packets occupy the link longer and can build up queues. In practice, queuing delay is mainly driven by congestion, but packet size influences it indirectly.

