**ZID**: z5518601
**Name**: Tianxiong Wu
## **Exercise 3: Using Wireshark to understand basic HTTP request/response messages (2.5 marks, include in your report)**
>[!note] Answer & Screenshots
>#### Question 1: What is the status code and phrase returned from the server to the client browser?
>
> #### Question 2: When was the HTML file the browser retrieves last modified at the server? Does the response also contain a DATE header? How are these two fields different?
> 
> #### Question 3: Is the connection established between the browser and the server persistent or non-persistent? How can you infer this?
> 
> #### Question 4: How many bytes of content are being returned to the browser?
> 
> #### Question 5: What is the data contained inside the HTTP response packet?
> 
> ![[Pasted image 20260301220651.png]]

## **Exercise 4: Using Wireshark to understand the HTTP CONDITIONAL GET/response interaction (2.5 marks, include in your report)**

> [!NOTE] Answer & Screenshots
> #### Question 1: Inspect the contents of the first HTTP GET request from the browser to the server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?
> 
> #### Question 2: Does the HTTP response from the server indicate the last time the requested file was modified?
> 
> #### Question 3: Now inspect the contents of the second HTTP GET request from the browser to the server. Do you see the “IF-MODIFIED-SINCE:” and “IF-NONE-MATCH” lines in the HTTP GET? If so, what information is contained in these header lines?
> 
> #### Question 4: What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the file's contents? Explain.
> 
> #### Question 5: What is the value of the Etag field in the 2nd response message, and how is it used? Is the Etag value the same as in the 1 st response?

## **Exercise 5: Ping Client (5 marks, submit source code as a separate file, include sample output in the report)**
