---
tags:
  - LectureNotes
---
## 1. SQL in Relational DBMS
### 1.1 DDL
A data definiton language
➢ CREATE TABLE, DROP TABLE, …
### 1.2 DML
A data manipulation language
➢ SELECT (keywords relating to select: GROUP BY, HAVING, ORDER BY…), INSERT, DELETE, UPDATE, ALTER, …
## 2. Sample Database
![[Pasted image 20241028211913.png]]
## 3. SQL Queries
```SQL
Queries
Select Name From Beers Where Manf='Toohey''s';
```
Quotes are escaped by doubling them ('')
### 3.1 Basic Select Structure
```SQL
select attribute from table where condition
```
### 3.2 Data Types
Strings, numbers, dates and bit-strings.
- Integer
	- smallint 2 byte integer
	- int 4 byte integer
	- bigint 8 byte integer
- Real numbers
	- real 4 byte floating point
	- double 8 byte floating point
	- numeric(precision,scale)
		- precision: specify significant digits in the whole number
		- scale: specify digits after the decimal point
- String Literal
	- string || string … concatenate two strings 字符串合并
	- LENGTH (string) ... return length of string 返回字符串长度
	- SUBSTR (string, start, length) ... extract chars from within a string 分割字符串
### 3.3 Like Operator
Two kinds of string pattern-matching 
➢ The symbol _ (underscore) matches any single characters 
➢ The symbol % (percent) matches zero or more characters
### 3.4 SQL Dates
>[!note] (start1, end1) OVERLAPS (start2, end2) 
➢ This expression yields true when two time periods (defined by their endpoints) overlap, false when they do not overlap.
### 3.5 Converting Data Types
SQL supports a small set of useful built-in data types, e.g., numbers, strings, dates, etc... ➢ You can define your own type in SQL.
### 3.6 Tuple and Set Literals
Tuple and set constants are both written as: (val1, val2, val3, ... ) 
The correct interpretation is worked out from the context. 
Examples: Student(stude#, name, course) ( 2177364, ’Jack Smith’, ’BSc’) -- tuple literal 
SELECT name FROM Employees WHERE job IN (’Lecturer’, ’Tutor’, ’Professor’); -- set literal