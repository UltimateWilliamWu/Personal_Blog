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
>
> #### 1.1 How many routers are there between your workstation and uni-heidelberg.de?
> 
> My traceroute output shows hops **1 to 17**. In the captured output, the last visible hop is already inside the **University of Heidelberg** network (`...uni-heidelberg.de`).  
> So, based on what is shown:
> - The path contains **17 hops/routers** up to the last router displayed (hop 17).
> - This indicates **17 routers on the path before reaching the destination host** (or at least before the destination host reply appears — the destination line is not visible in the screenshot).
>     
> #### 1.2 Identify the routers which are part of the UNSW network?
> 
> These hops are clearly within UNSW (based on `unsw.edu.au`, UNSW IP ranges, and private RFC1918 addressing):
> 
> - **Hop 1:** `vlan380.cse.unsw.EDU.AU (129.94.208.1)` → UNSW (CSE VLAN gateway)
>     
> - **Hop 2:** `129.94.39.17` → UNSW (129.94.0.0/16 is UNSW)
>     
> 
> #### 2. Which router is the first router outside of Australia?
> 
> The first hop that is clearly outside Australia is:
> 
> - **Hop 10/11:** `...bdr1.sing.sin.aarnet.net.au (113.197.15.231)`  
>     The hostname contains **`sing.sin`**, which strongly indicates **Singapore**.
>     
> 
> This is also supported by RTT behavior:
> 
> - RTT is ~**46 ms** around hop 9–10 (Australia backbone)
>     
> - RTT jumps to ~**92 ms** at the Singapore AARNet router (hop 10/11), consistent with an international link.
>     
> 
> So the **first router outside Australia is the AARNet Singapore router** (113.197.15.231).
> #### 3. Try to identify the approximate locations of the routers.
> ![[Pasted image 20260224211514.png]]

2. Run a traceroute from your machine to the following destinations: (i) [www.nyu.edu](http://www.nyu.edu/) (ii) [www.aut.ac.nz](http://www.aut.ac.nz/) and (iii) [www.nottingham.ac.uk](http://www.nottingham.ac.uk/)

>[!note] Answer & Screenshots
>#### 1. Last common router (where the three paths diverge)
> 
> The **last hop that is common to all three destinations is hop 2**:
> 
> - **Hop 2:** `129.94.39.17`
>     
> 
> After that they diverge:
> 
> - **NYU** goes to `172.17.47.11` at hop 3
>     
> - **AUT** goes to `172.17.47.11` at hop 3
>     
> - **Nottingham** goes to `172.17.47.2` at hop 3 (different)
>     
> 
> So the **paths diverge at hop 3**, meaning **hop 2 is the last router they have in common**.
> ![[Pasted image 20260224213200.png]]
> #### 2. Is hop count proportional to physical distance?
> **No, not necessarily.** Hop count depends on routing policy (BGP), peering, MPLS, filtering, and how many layer-3 hops reply to TTL-expired probes—not just geography.

3. Several servers are distributed worldwide to provide a web interface from which you can perform a traceroute to any other host on the Internet. Here are two examples: (i) [http://lg.nexlinx.net.pk/](http://lg.nexlinx.net.pk/) and (ii) [www.as13030.net/traceroute.php](http://www.as13030.net/traceroute.php) .

>[!note] Answer & Screenshots
>![[Pasted image 20260224214217.png]]
>![[Pasted image 20260224214250.png]]
>#### 1. What are the IP addresses of the two servers that you have chosen?
>The IP addresses of the two looking-glass servers are **202.59.80.52 (lg.nexlinx.net.pk)** and **213.144.137.198 (as13030.net)**, as shown in the first line of my traceroute outputs.
>#### 2. Does the reverse path go through the same routers as the forward path?
>![[Pasted image 20260224220336.png]]
>![[Pasted image 20260224220904.png]]
>The reverse path does **not** traverse exactly the same set of routers as the forward path. This is expected due to **asymmetric routing** on the Internet, where BGP policies and peering arrangements may select different routes in each direction.
>#### 3. If you observe common routers between the forward and the reverse path, do you also observe the same IP addresses? Why or why not?
>No, some parts of the forward and reverse paths traverse common networks (e.g., Zayo `64.125.*` and AARNet `113.197.15.*`). However, even when a router is “common”, the **observed IP address may not be identical**. Traceroute shows the IP address of the interface that sends the ICMP reply, and routers have multiple interfaces; different interfaces may be used in each direction. In addition, ECMP load balancing, ICMP rate-limiting, and MPLS tunneling can cause some hops to appear as `* * *` or appear with different IPs across runs.

## **Exercise 4: Use ping to gain insights into network performance (4 marks)**
>[!note] Answer & Screenshots
>1. For each location, ﬁnd the (approximate) physical distance from UNSW . You can use a site like [Distance Calculator](https://www.distancecalculator.net/) , [Google Maps](https://www.google.com/maps) , or whatever you prefer to take this measurement. Then, compute the shortest possible time T for a packet from UNSW to reach that location. You should assume that the packet moves (i.e. propagates) at the speed of light, 3 x 10^8 m/s. Note that the shortest possible time will be the distance divided by the propagation speed.
> 2. Plot a graph where the x-axis represents the distance to each city (i.e. **New York, USA** , **Auckland, New Zealand** and **Nottingham, UK** ). The y-axis represents the ratio between the minimum delay (i.e. RTT) measured by the ping program (select the values for 50-byte packets) and the shortest possible time T to reach that city from UNSW. (Note that the y-values are no smaller than 2 since it takes at least 2*T time for any packet to reach the destination from UNSW and return).You can also use the provided [generate_plot.py](https://webcms3.cse.unsw.edu.au/COMP3331/26T1/resources/118373) to generate the plot. Download (to Vlab or personal machines with Python 3 installed). Open the [generate_plot.py](https://webcms3.cse.unsw.edu.au/COMP3331/26T1/resources/118373) and uncomment the designated lists, and replace them with the actual values.Can you think of at least two reasons why the y-axis values you plot are greater than 2?
> 3. Is the delay to the destinations constant, or does it vary over time? Explain why.
> 4. The measured delay (i.e., the delay you can see in the graphs) comprises propagation, transmission, processing, and queuing delays. Which of these delays depend on the packet size and which do not?


