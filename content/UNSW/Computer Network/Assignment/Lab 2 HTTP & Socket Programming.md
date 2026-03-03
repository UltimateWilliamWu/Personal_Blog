---
tags:
  - Assignment
---
**ZID**: z5518601
**Name**: Tianxiong Wu
##  **Exercise 3: Using Wireshark to understand basic HTTP request/response messages (2.5 marks, include in your report)**

>[!note] Answer & Screenshots
>#### **Question 1: What is the status code and phrase returned from the server to the client browser?**
>The server returns status code **200** with the phrase **“OK”**.
>
>![[Pasted image 20260303102131.png]]
> #### **Question 2: When was the HTML file the browser retrieves last modified at the server? Does the response also contain a DATE header? How are these two fields different?**
> The HTML file was last modified on **Tue, 23 Sep 2003 05:29:00 GMT** (from the Last-Modified header). The response also contains a Date header: **Tue, 23 Sep 2003 05:29:50 GMT**.
> Last-Modified indicates when the requested resource (the HTML file) was last changed on the server, whereas Date indicates when the server generated/sent this HTTP response. In this trace, Date is 50 seconds later than Last-Modified, so they refer to different timestamps (resource modification time vs. response time).
> #### **Question 3: Is the connection established between the browser and the server persistent or non-persistent? How can you infer this?**
> The connection is **persistent**. This is inferred from the response headers showing **Connection: Keep-Alive** and **Keep-Alive: timeout=10, max=100**, which indicates the TCP connection is kept open for additional HTTP requests/responses rather than being closed after this single response.
> In contrast, a non-persistent connection would typically include _Connection: close_ and the TCP connection would be closed immediately after the response.
> #### **Question 4: How many bytes of content are being returned to the browser?**
> The server returns 73 bytes of content. This is indicated by the **Content-Length: 73** header in the HTTP/1.1 200 OK response.
> #### **Question 5: What is the data contained inside the HTTP response packet?**
> The data contained inside the HTTP response packet is the HTML content of the requested page (lab2-1.html). In this trace, Wireshark shows the response body as line-based text data (text/html), containing:
> ```html
><html> 
>Congratulations. You've downloaded the file lab2-1.html! 
></html>
>```
>![[Pasted image 20260303104300.png]]


## **Exercise 4: Using Wireshark to understand the HTTP CONDITIONAL GET/response interaction (2.5 marks, include in your report)**

> [!NOTE] Answer & Screenshots
> #### Question 1: Inspect the contents of the first HTTP GET request from the browser to the server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?
> No. The first HTTP GET request does not contain an **If-Modified-Since** header.
> 
> ![[Pasted image 20260303105701.png]]
> #### Question 2: Does the HTTP response from the server indicate the last time the requested file was modified?
> Yes. The server’s first HTTP response includes a **Last-Modified** header indicating the file was last modified on Tue, 23 Sep 2003 05:35:00 GMT.
> 
> ![[Pasted image 20260303105856.png]]
> #### Question 3: Now inspect the contents of the second HTTP GET request from the browser to the server. Do you see the “IF-MODIFIED-SINCE:” and “IF-NONE-MATCH” lines in the HTTP GET? If so, what information is contained in these header lines?
> Yes. The second HTTP GET request includes both conditional headers:
> - **If-Modified-Since**: Tue, 23 Sep 2003 05:35:00 GMT. This is a timestamp indicating the last modification time of the cached copy (used to ask the server to return the file only if it has been modified after this time).
> - **If-None-Match**: "1bfef-173-8f4ae900". This contains the ETag (entity tag) value previously provided by the server, used to validate whether the cached version matches the current server version.
>
> ![[Pasted image 20260303110402.png]]
> #### Question 4: What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the file's contents? Explain.
> 
> The server returns HTTP status code 304 with the phrase “Not Modified” (HTTP/1.1 304 Not Modified) in response to the second GET. The server did not explicitly return the file’s contents; instead, 304 indicates the resource has not changed since the time/ETag provided in **If-Modified-Since** and **If-None-Match**, so the browser should use its cached copy.
> 
>  ![[Pasted image 20260303114502.png]]
> #### Question 5: What is the value of the Etag field in the 2nd response message, and how is it used? Is the Etag value the same as in the 1 st response?
> The ETag value in the 2nd response (the 304 Not Modified response) is "1bfef-173-8f4ae900". The ETag is used as a cache validator: the browser sends it in the **If-None-Match** header in a subsequent request, and the server compares it with the current ETag of the resource. If they match, the server concludes the resource has not changed and can return 304 Not Modified without sending the file body.
>Yes, the ETag value is the same as in the 1st response (the 200 OK response), which also has **ETag: "1bfef-173-8f4ae900"**.

## **Exercise 5: Ping Client (5 marks, submit source code as a separate file, include sample output in the report)**
