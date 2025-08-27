---
tags:
  - LectureNotes
---
## 1. Relational Data Model
>[!note] Definition
>The relational data model describes the world as 
>➢ a collection of inter-connected relations
>The relational model has two styles of terminology: 
>➢ **mathematical**: relation, tuple, attribute, ... 
>➢ **data-oriented**: table, record, field/column, ...
### 1.1 Structures
In the relational model, everything is described as relations.
A relation can be thought of as a named table.
- Each column of the table corresponds to a named attribute.
- Each row of the table is called a **tuple** of the relation.
The set of allowed values for an attribute is called its domain.
**Composite and multivalued attributes are not allowed!**
**Relations are unordered** 
### 1.2 Keys
A **superkey** is a set of attributes that uniquely determines a tuple. 
A **candidate key** is a minimal superkey, i.e., none of whose subsets is a superkey.
A **primary key** is a designated candidate key.
Number of Superkeys:
$$(2^n)-1$$
**Foreign key**: an attribute that keeps the value of a primary key of another relation.
### 1.3 Relational Integrity Constraints
Three integrity constraints are important:
1. **Key constraint**: candidate key values must be unique for every relation instance.
2. **Entity integrity**: an attribute that is part of a primary key cannot be NULL.
3. **Referential integrity**: The value of FK must occur in the other relation or be entirely NULL.
Valid state: a relation does not violate any integrity constraints. 
Invalid state: a relation violates at least one integrity constraint
### 1.4 ER to Relational Data Model Mapping
Step 1: For each strong entity (not weak entity) type E, create a new relation R with 
➢ Attributes: all simple attributes (and simple components of composite attributes) of E. 
➢ Key: key of E as the primary key for the relation.

Step 2 : For each weak entity type W with the owner entity type E, create a new relation R with – Attributes :
- all simple attributes (and simple components of composite attributes) of W, – and include the primary key attributes of the relation derived from E as the foreign key. 
-  Key of R: foreign key to E and partial key of W.

Step 3 : For each 1:1 relationship type B. Let E and F be the participating entity types. Let S and T be the corresponding relations. 
- Choose one of S and T (let S be the one that participates totally if there is one). 
- Add attributes from the primary key of T to S as a foreign key. 
- Add all simple attributes (and simple components of composite attributes) of B as attributes of S.

Step 4 : For each 1:N relationship type B. Let E and F be the participating entity types. Let S and T be the corresponding relations. Let E be the entity on the 1 side and F on the N side. 
Add to the relation belonging to entity T, 
- the attributes from the primary key of S as a foreign key. 
- any simple attributes (or simple components of composite attributes) from relationship B. (Notice that this doesn’t add any new tuples, just attributes.)

Step 5: For each N:M relationship type B. Let E and F be the participating entity types. Let S and T be the corresponding relations 
Create a new relation R (cross-reference) with Attributes : 
- Attributes from the key of S as a foreign key, 
-  Attributes from the key of T as a foreign key, 
- Simple attributes and simple components of composite attributes of relation B. 
- Key: All attributes from the key of S and T.

Step 6: For each multivalued attribute A, where A is an attribute of E, create a new relation R. 
➢ If A is a multivalued simple attribute, 
	➢ Attributes of R = Simple attribute A, and key of E as a foreign key. 
➢ If A is a multivalued composite attribute, 
	➢ Attributes of R = All simple components of A, and key of E as a foreign key. 
In both cases, the primary key of R is the set of all attributes in R.

Step 7: For each N-ary relationship type (n > 2), create a new relation with 
➢ Attributes: same as Step 5. 
➢ Key: same as Step 5 (Advice: binary relationships are simpler to model.)
## 2. Relational Algebra
>[!note] Introduction
>Relational Algebra is a procedural data manipulation language (DML).
>- Unary Relational Operations: Select, Project 
>- Operations from Set Theory: Union, Intersection, Difference, Cartesian Product 
>- Binary Relational Operations: Join, Divide.
### 2.1 Select
Notation: 𝜎<𝑠𝑒𝑙𝑒𝑐𝑡𝑖𝑜𝑛 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛>(𝑅) Intuition: Filters out all tuples that do not satisfy select condition
Selection Condition: 
The condition is defined by a selection clause: 
Where operator is one of =, <, ≤, >, ≥ or ≠ …
Selection clauses can also be 
Terms equivalently expressed by ∧ (and), ∨(or), ¬ (not)
eg.if there is a table named Enrolment then **𝜎 𝑆𝑢𝑝𝑒𝑟𝑣𝑖𝑠𝑜𝑟=1 ( ENROLMENT)** means specifiying all Supervisor where value is equal to 1
#### Properties of Selection
➢ Consecutive selects can be combined:
$$𝜎_{<cond1>}(𝜎_{<cond2>}(R))=𝜎_{<cond1> AND <cond2>}(R)$$
➢ Selection is a commutative operation:
$$𝜎_{<cond1>}(𝜎_{<cond2>}(R))=𝜎_{<cond2>}(𝜎_{<cond1>}(R))$$
### 2.2 Project
The PROJECT operation is used to project a subset of the attributes (column) of a relation, denoted by:
$$𝜋_{<attribute list>}(R)$$
### 2.3 Set Union
Condition: R and S must be union compatible! 
Union compatibility: **==there is a 1-1 correspondence between their attributes: the same name and same domain.==**
$$R \cup S = \{ t:t \in R \:or\: t \in S \} $$
### 2.4 Set Intersection
INTERSECTION is an operation that includes all tuples that are in present both relations, denoted by
$$ R \cap S=\{t:t\in R \:and\: t \in S\} $$
Condition: R and S must also be union compatible!
### 2.5 Set Difference
DIFFERENCE is a relation that includes all tuples that are in the left relation but not in the right relation, denoted by
$$ R-S=\{t:t\in R \:and\: t\not\in S\}$$
Condition: R and S must also be union compatible!
### 2.6 Cartesian Product
$$R \times S=\{t_1||t_2:t_1\in R \:and\: t_2 \in S\}$$
Intuition: every combination of tuples in R with tuples in S.
- 𝑡1 || 𝑡2 indicates the concatenation(连接) of tuples.
- R and S not required to be union compatible
- The number of tuples in the output relations is always |𝑅| ∗ |𝑆|
### 2.7 Join
JOIN is used to combine related tuples from two relations into single "longer" tuples.
**Theta-join**:
$$ R\Join_{<join\: condition>} S=\{t_1||t_2:t_1\in R \: and \: t_2\in S \:and\: <join\:condition>\}$$
#### 2.7.1 Equi-join
A type of theta-join where the only comparison operator used is “=” is called an Equi-join
Example:
$$ENROLMENT\Join_{(Supervisor=Person)}RESEARCHER$$
#### 2.7.2 Natural Join
A type of equi-join that requires each pair of join attributes to have the same name and domain in both relations. 
Notes: In a natural join, there may be several valid pairs of join attributes.
$$ENROLMENT\Join_{(department,name),(department,name)}COURSE$$
If there are pairs of joining attributes identically named, we can write:
$$ENROLMENT\Join COURSE$$
### 2.8 Divide
The DIVISION operation is applied to two Relations R and S, where the attributes of S are a subset of the attributes of R.
![[Pasted image 20241028201336.png|475]]
Typical use: which courses are offered by all departments?
$$ Course\div (𝜋_{Deparment} Course)$$
### 2.9 Rename Operator
The rename operator ρ changes the name of one or more attributes
### 2.10 Aggregate Operators
![[Pasted image 20241028202245.png|575]]
