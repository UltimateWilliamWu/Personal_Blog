---
tags:
  - LectureNotes
---
# Week_1.1 Introduction about DBMS
Data contains the following features:
- stored 
- manipulated/accessed
- shared
- ==transmitted== 
Except transmitted is handled by networks others are handled by databases;

>[!info] Definitions
 **Database**: Collection of related data that models some aspect of the real world.
> **Data**: known facts that can be recorded and have implicit meaning ...
>- Unstructured Data
>- Structured Data
>
> **Database Management System (DBMS)**: ... a collection of programs that enables users to create and maintain a database ...
> **Database System**: ... The database and DBMS together ...
> **Data model**: concepts used to describe the allowed structure of a database. i.e., the structure of the meta-data.
> **Data definition language (DDL)**: used to define the conceptual schema. 
> **Data manipulation languages (DML)**: let users write requests to retrieve and manipulate data, as well as other tasks relating to data manipulation.
> **Database Schema**: a formalism of the data model, the structural description of what information will database holds. 
> **Database Instance (or State)**: any combination of actual information populated in the database at a particular time.

>[!question] Why Database Systems not File Systems?
>Drawbacks of using file systems to store data: 
>➢ **Data redundancy and inconsistency**  
>- Multiple file formats, duplication of information in different files
>
>➢ **Difficulty in accessing data** 
>- Would have to write a new program to carry out each new task )
>
>➢ **Data isolation — multiple files and formats**
>
>➢ **Integrity problems **
>-  Integrity constraints (e.g., account balance >= 0) become “buried” in program code rather than being clearly kept and stated 
>-  Hard to add new constraints or change existing ones
>
>➢**Atomicity of updates**
>- What is computer crashes? ◦
>- Failures may leave the data in an inconsistent state. 
>-  Example: Transfer of funds from one account to another should either complete or not happen at all
>
>➢**Hard to allow concurrent access by multiple users**

>[!note] DBMS Features
>➢ Data Independence 
>➢ Efficient Data Access 
>➢ Data Integrity and Security
>➢ Data Administration 
>➢ Concurrent Access and Crash Recovery 
>➢ Reduced Application Development Time


![[Pasted image 20240917233019.png]]
# Week_1.2 Data Modelling, ER Diagram
## 1. Data Modelling
Kinds of data models:
-  conceptual: abstract, ER, ODL
-  logical: concrete, implementation of specific DBMS
-  physical: internal file storage
### 1.1 Conceptual Design (ER Diagram)
> [!Important] ER Features
> # Soultion
> - ## Entities: 
> **-- Entity: collection of attributes describing object of interest.**
> 	1. Entity Type (实体型)
>--- Defines a collection of entities that have the same attributes.
> 	2. Entity Instance (实体)
>---  A good entity schema should have good attributes that can be filled with good values.	
> 	3. Entity Set (实体集)
> --- Defines a collection of entity type that have the same attributes.
> 	4. Weak Entity (弱实体)
> --- Some entity types do not have a key of their own.
> - ## Relationships
> **-- Relationships association between entities.**
> **-- Cardinality ratio: the number of relationship instances an entity can participate in.**
> - ## Attributes
> **-- data item describing a property of interest**
> 	1. Simple Attributes: attributes that are not divisible (etc. Entity= Student Attributes=Student number)
> 	2. Multi-Valued Attributes:  has more than one value (etc. Entity=T-shirts Attributes=Color)
> 	3. Composite Attributes: can be divided into smaller subparts (etc. Address)
> 	4. Derived Attributes: Attributes that are problematic if modeled with a simple value. (etc. Birth)
> - ## Key 
> ** -- Key constraint in ER Modelling: in any extension of the entity type, no two entities have the same values for their key attribute or key attributes. **
>  - Key/Super key: A super key is a set of one or more attributes that uniquely identify any entity instance of an entity type.
> - Candidate key: minimal superkey (no subset is a key)
> - Primary key: a candidate key chosen by DB designer
> ![[Pasted image 20240911202705.png|425]]
## 1.2 Modelling relationships
#### 1.2.1 Participation Constraint on Relationships
**Total Participation: each entity instance must particiate in at least one relationship instance.**
- Example: We want this relationship to express all publications must be written by a person.
![[Pasted image 20241028210303.png]]
**Partial Participation: not necessarily total.**
- Example: Not every person has publication
