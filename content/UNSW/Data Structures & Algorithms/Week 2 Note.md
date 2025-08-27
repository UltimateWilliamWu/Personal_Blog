---
tags:
  - LectureNotes
---
[[ProblemSets 2.1]]
[[ProblemSets 2.2]]
## 1. Pseudocode
- More structured than English prose
- Less detailed than a program
- Preferred notation for describing  algorithms
- Hides program design issues
## 2. The Abstract RAM Model
RAM=Random Access Machine
- A CPU
- A potentially unbounded bank of memory cells
	- each of which can hold an arbitary(孤立的) number, or character
- Memory cells are numbered, and accessing any one of them takes CPU time
## 3. Primitive Operations
- Basic computations performed by an algorithm
- Identifiable in pseudocode
- Largely independent of the programming language
- Exact definition not important (we will shortly see why)
- Assumed to take a constant amount of time in the RAM model
Example:
```
arrayMax(A): 
	Input array A of n integers 
	Output maximum element of A 
	currentMax=A[0]                   1
	for all i=1..n-1 do               n+n-1     
		if A[i]>currentMax then       2(n-1)  
			currentMax=A[i]           n-1 
		end if 
	end for 
	return currentMax                 1
```
## 4. Estimating Running Times
Seven commonly encountered functions for algorithm analysis
- Constant=1
- Logarithmic $\approx$ log n
- Linear $\approx$ n
- N-Log-N $\approx$ n log n
- Quadratic $\approx n^2$
- Cubic $\approx n^3$
- Exponential $\approx 2^n$
```
matrixProduct(A,B):
	Input n×n matrices A, B
	Output n×n matrix A·B
	for all i=1..n do
		for all j=1..n do
			C[i,j]=0
			for all k=1..n do
				C[i,j]=C[i,j]+A[i,k]·B[k,j]
			end for
		end for
	end for
	return C
```
[[Week2.pdf#page=4&annotation=257R|Week2, p.4]]
> for all i=1..n do //循环n次 判断n+1次 相加得2n+1
> for all j=1..n do //将2n+1代入n 循环2n+1次与循环n次相乘 得n(2n+1)
> C[i,j]=0  //执行1次 与上两层循环相乘得$n^2$
> for all k=1..n do //将n(2n+1)代入n 并与循环n次相乘得$n^2(2n+1)$
> C[i,j]=C[i,j]+A[i,k]·B[k,j] //读取A,B, 计算乘积最后与C相加  一共四次操作
## 5. Big-Oh Notation
- Big-Oh notation gives an upper bound on the growth rate of a function(上界)
	- O(g(n)) if f(n) is asymptotically less than or equal to g(n)
	 - Ω(g(n)) if f(n) is asymptotically greater than or equal to g(n)
	-  Θ(g(n)) if f(n) is asymptotically equal to g(n)
- Use the smallest possible class of functions(忽略参数)
- Use the simplest expression of the class(忽略多项式)
## 6. Static/Dynamic Sequences
### 6.1 Linklist
```C
typedef struct node{
	int data;
	struct node *next; //指向数据结构的指针
}Node;//数据结构整体
//创建头节点 即指向数据的头指针
Node* creatList()
{
    Node *headNode = (Node *)malloc(sizeof(Node));
    //变量使用前必须被初始化
    //headNode->data = 1;  创建空表头
    headNode->next = NULL;
	
    //返回表头地址
    return headNode;	
}
//创建节点
Node* creatNode(int data)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    
    //通过函数的形参写入节点的数据
    newNode->data = data;
    newNode->next = NULL;

    return newNode;
}

void insertNodeByHead(Node *headNode, int data)
{
    //创建插入的节点，创建节点的同时对其数据域赋值
    Node *newNode = creatNode(data);
    newNode->next = headNode->next;//此时newNode—>next ==NULL
    headNode->next = newNode;
}

void insertNodeByTail(Node *headNode, int data)
{
    Node *newNode = creatNode(data);
    //找到表尾
    Node *tailNode = headNode;
    while (tailNode->next != NULL)
    {
        tailNode = tailNode->next;

    }
    tailNode->next = newNode;
    //找到表尾
}

void insertNodeByPos(Node *headNode, int insertData, int posData)
{
    Node *posNodeFront = headNode;//目标节点的前驱节点
    Node *posNode = headNode->next;//目标节点
    if (posNode == NULL)
    {
        printf("链表为空\n");
        return;
    }
    else
    {
        while (posNode->data != posData)
        {
            posNodeFront = posNode;
            posNode = posNode->next;
            if (posNode == NULL)
            {
                printf("未找到该数据\n");
                return;
            }
        }
        Node *newNode = creatNode(insertData);
        newNode->next = posNode;
        posNodeFront->next = newNode;
    }
    
void deleteNodeByHead(Node *headNode) //传递的指针是删除节点前驱节点
{
    Node *deleteNode = headNode->next;
    headNode->next = deleteNode->next;
    free(deleteNode);
    deleteNode = NULL;
}

void changeNode(Node *headNode, int changeData, int posData)
{
    Node *p = headNode->next;
    if (p == NULL)
    {
        printf("链表为空.\n");
        return;
    }
    else
    {
        while (p->data != posData)
        {
            p = p->next;
            if(p == NULL)
            {
                printf("没有找到该数据.\n");
                return;
            }
        }
        p->data = changeData;
    }
}
```
### 6.2 Comparison Array vs Linked List
Complexity of operations, n elements

|                            | array                              | linked list                                  |
| -------------------------- | ---------------------------------- | -------------------------------------------- |
| insert/delete at beginning | O(n)                               | O(1)                                         |
| insert/delete at end       | O(1)                               | O(1) doubly-linked list with pointer to rear |
| insert/delete at middle    | O(n)                               | O(n)                                         |
| find an element            | O(n) / O(log n) if array is sorted | O(n)                                         |
| index a specific element   | O(1)                               | O(n)                                         |
## 7. Complexity Classes
Classes of problems: 
- P = problems for which an algorithm can compute answer in polynomial time 
- NP = includes problems for which no P algorithm is known 
Beware: NP stands for "nondeterministic, polynomial time (on a theoretical Turing Machine)"
## 8. Memory
Reminder: Computer memory … large array of consecutive 
data cells or bytes 1 byte = 8 bits = 0x00 … 0xFF char … 1 byte int,float … 4 bytes double … 8 bytes
## 9. Pointer
A pointer … 
- is a special type of variable 
- storing the address (memory location) of another variable
### 9.1 Pointer Arithmetic
For a pointer declared as T $*$p; (where T is a type) 
- if the pointer initially contains address A executing p = p + k; (where k is a constant) 
	- changes the value in p to A + k$*$sizeof(T) 
The value of k can be positive or negative.
Example:
``` 
int a[6]; (addr 0x1000)      char s[10]; (addr 0x2000) 
int *p; (p == ?)             char *q; (q == ?) 
p = &a[0]; (p == 0x1000)     q = &s[0]; (q == 0x2000) 
p = p + 2; (p == 0x1008)     q++; (q == 0x2001)
```
### 9.2 Arrays of Strings
main() needs different prototype if you want to access command-line arguments: 
int main(int argc, char $*$argv[]) { ... 
- argc … stores the number of command-line arguments + 1 
	- argc == 1 if no command-line arguments 
- argv[] … stores program name + command-line arguments 
	- argv[0] always contains the program name 
	- argv[1],argv[2],… are the command-line arguments if supplied 
<stdlib.h> defines useful functions to convert strings:
- atoi(char $*$s) converts string to int 
- atof(char $*$s) converts string to double (can also be assigned to float variable)
### 9.3 Pointers and Structures
```C
typedef struct{
	char name[60];
	Date birthday;
	int status;
	float salary;
}WorkerT;
WorkerT w; WorkerT *wp;
wp=&w;
*wp.salary=125000.00;//error!!!
w.salary = 125000.00; // because it is interpreted as 
*(wp.salary) = 125000.00; // error!!!to achieve the correct effect, we need 
(*wp).salary = 125000.00; // a simpler alternative is normally used in C
wp->salary=125000.00;
```
### 9.4 C execution: Memory
An executing C program partitions memory into: 
- code … fixed-size, read-only region (代码区)
	- contains the machine code instructions for the program 
- global data … fixed-size (常量区)
	- contain global variables (read-write) and constant strings (read-only) 
- heap … very large, read-write region (堆)
	- contains dynamic data structures created by malloc() (see later) 
- stack … dynamically-allocated data (function local vars) (栈)
	- consists of frames, one for each currently active function 
	- each frame contains local variables and house-keeping info
## 10. Memory Management
### 10.1 Using malloc
malloc() returns a pointer to a data object of some kind. 
Things to note about objects allocated by malloc(): 
- they contain random values 
	- need to be initialised before they are read 
- they exist until explicitly removed (program-controlled lifetime) 
- they are accessible while some variable references them 
- if no active variable references an object, it is garbage 
The function free() releases objects allocated by malloc()
### 10.2 Memory Leaks
Well-behaved programs do the following: 
- allocate a new object via malloc() 
- use the object for as long as needed 
- free() the object when no longer needed 
A program which does not free() each object before the last reference to it is lost contains a memory leak. 
Such programs may eventually exhaust available heapspace.