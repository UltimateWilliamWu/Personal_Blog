# **1. What are the main aspects of data quality? (page 8)**

The usual way to think about data quality is through a few simple dimensions:  
whether the data is correct (accuracy), whether anything important is missing  
(completeness), whether the same entity appears only once (uniqueness),  
whether the data is up-to-date (timeliness), and whether the dataset is internally  
consistent (consistency).

---

# **2. Why is “understanding the data” always the first step in a data project? (page 4)**

Because without knowing what the dataset represents, what fields exist, how they  
relate to the domain, and what questions we’re trying to answer, any later  
cleaning or modelling will be blind. Understanding the schema and context  
basically tells you how to process the data meaningfully.

---

# **3. What are some common data-cleaning tasks? (page 9)**

Typical things include dealing with missing values, removing irrelevant or  
unhelpful rows and columns, and fixing formatting issues like date formats or text  
inconsistencies.

---

# **4. What’s the difference between merging data and grouping data? (page 10)**

Merging is about combining information from different tables or datasets based  
on shared keys. Grouping is about taking one dataset and summarizing it by some  
category — for example, computing averages per region or counts per day.

---

# **5. What are the key constraints of REST? (page 15)**

REST follows a few basic ideas: the client and server stay separate, the interface  
should be uniform, the server keeps no session state between requests, responses  
can be cached, the system can be layered, and downloadable code is optional.  
These constraints help keep REST services simple, scalable, and predictable.

---

# **6. In REST, what does “stateless” actually mean? (page 30)**

It simply means that each request must contain everything the server needs to  
process it. The server doesn’t remember anything about earlier requests from the  
same client. This makes scaling and load-balancing much easier.

---

# **7. What are the essential parts of an HTTP response?**

A proper response starts with a status line, followed by headers, and then the  
response body. That’s all you need.

---

# **8. Write a reasonable HTTP response to this POST request. (page 31)**

```
HTTP/1.1 201 Created
Location: /orders/123
Content-Type: application/xml

<order>
    <id>123</id>
    <drink>latte</drink>
</order>
```

---

# **9. How do authentication and authorization differ? (page 18)**

Authentication answers “Who are you?”, while authorization answers “What are  
you allowed to do?”. In HTTP terms, a failed authentication gives you 401, while a  
user who is authenticated but not allowed to access something gets 403.

---

# **10. Why should REST APIs use HTTPS? (page 17)**

Because HTTPS protects confidentiality and integrity and prevents  
man-in-the-middle attacks. It’s basically the only safe way to exchange sensitive  
information over the internet.

---

# **11. What are some common API authentication methods? (page 18)**

People often use Basic Authentication, tokens, API keys (sometimes with  
signatures), or OAuth for more complex authorisation flows.

---

# **12. What does a typical machine-learning workflow look like? (page 21)**

It usually starts with defining a model, training it, validating it on held-out data,  
using or deploying it, and then periodically updating and retraining it as new data  
arrives.

---

# **13. What do you need in order to perform clustering?**

Clustering doesn’t require labels — that’s the point — but it does require some  
kind of feature representation for each item. You need meaningful numeric  
features so the algorithm can detect patterns or group similarities.

---

# **14. What information is needed to build a recommender system? (page 23)**

You need something describing the user — ratings, preferences, demographics,  
or context — along with information about the items. Using these, the system  
computes a relevance score and recommends items with high scores.

---

# **15. Suppose you want to predict fuel prices using two CSV files: one with fuel prices and one with crude-oil prices. Describe how you would approach this. (page 32)**

I’d start by looking at both datasets to understand their structure and make sure  
the date fields line up. Then I’d clean them: fix missing values, drop useless  
columns, and convert dates to usable formats. After that, I’d merge both files by  
date so each record contains both fuel and crude-oil prices.  
For modelling, something straightforward like a regression model works well  
because the relationship between crude-oil price and fuel price is reasonably  
direct. If needed, I’d create features such as lagged crude-oil prices to capture  
time effects. Then I’d train the model, validate it, and use it to forecast future fuel  
prices.

---

# **16. How would you briefly contrast REST with GraphQL?**

REST exposes multiple endpoints, each returning a fixed representation of a  
resource. GraphQL uses a single endpoint where the client specifies exactly what  
fields it wants, so it avoids over-fetching and under-fetching. REST is simpler and  
follows natural web semantics, while GraphQL is more flexible but requires a  
schema and resolvers.
