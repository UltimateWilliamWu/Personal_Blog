---
tags:
  - LectureNotes
---
[[ProblemSets 3]]
## 1. Graph Definitions
Many applications require 
- a collection of items (i.e. a set) 
- relationships/connections between items 
Examples: 
- maps: items are cities, connections are roads 
- web: items are pages, connections are hyperlinks 
Collection types you're familiar with 
- arrays and lists … linear sequence of items 
Graphs are more general … allow arbitrary connections
## 2. Properties of Graphs
Terminology(术语): |V| and |E| normally written as V and E.

> [!tip] Graph Terminology
>   A graph with V vertices has at most V(V-1)/2 edges.
>The ratio E:V can vary considerably. 
> - if E is closer to $V^2$, the graph is dense(稠密图)
> - if E is closer to V, the graph is sparse(稀疏图)
> Example: web pages and hyperlinks, intersections and roads on street map
> [[Week3.pdf#page=1&selection=248,1,256,6|Week3, p.1]]
> 
For an edge e that connects vertices v and w
>- v and w are adjacent (neighbours) 
>- e is incident on both v and w (入射边)
>
Simple path: 
>- a path where all vertices and edges are different
>
>Connected graph
>- there is a path from each vertex to every other vertex 
>- if a graph is not connected, it has ≥2 connected components
>
>Complete graph
>- there is an edge from each vertex to every other vertex 
>- in a complete graph, E = V(V-1)/2
>
>Spanning tree: tree containing all vertices(生成树 包含所有结点)
>A spanning tree of connected graph G = (V,E)
> - is a subgraph of G containing all of V 
> - and is a single tree (connected, no cycles) 
> A spanning forest of non-connected graph G = (V,E) 
> - is a subgraph of G containing all of V and is a set of trees (not connected, no cycles), with one tree for each connected component
> 
>n-Clique: complete subgraph on n nodes(n个结点完整子图)
## ==3. Graph Representations==
### 3.1 Array-of-edges Representation(边集数组)
Edges are represented as an array of Edge values (= pairs of vertices) (空间消耗为理论总边数目 $V(V-1)/2$ 乘以存储两个顶点空间大小)
- disadvantage: deleting edges is slightly complex 
- undirected: order of vertices in an Edge (v,w) doesn't matter

> [!tip] Cost Analysis
> Storage cost: O(E)
> Cost of operations: 
> - initialisation: O(1) 
> - insert edge: O(1) (assuming edge array has space) 
> - find/delete edge: O(E) (need to find edge in edge array) 
> 
> If array is full on insert 
> - allocate space for a bigger array, copy edges across ⇒ O(E) 
> 
> If we maintain edges in order 
> - use binary search to insert/find edge ⇒ O(log E) (requires binary search tree of edges → week 4)
> 
### 3.2 Adjaceny Matrix Representation(邻接矩阵)
Edges represented by a V × V matrix(消耗空间为指针个数乘以指针大小加上 $V^2$ 乘以存储单个顶点空间的大小)
- easily implemented as 2-dimensional array 
- can represent graphs, digraphs and weighted graphs 
	graphs: symmetric boolean matrix 
	digraphs: non-symmetric boolean matrix 
	weighted: non-symmetric matrix of weight values

> [!tip] Cost Analysis
> Storage cost: $O(V^2)$
> If the graph is sparse, most storage is wasted. 
> Cost of operations: 
> - initialisation: $O(V^2)$ (initialise V×V matrix) 
> - insert edge: O(1) (set two cells in matrix) 
> - delete edge: O(1) (unset two cells in matrix)
### 3.3 Adjacency List Representation(邻接表)
- relatively easy to implement in languages like C 
- can represent graphs and digraphs 
- memory efficient if E:V relatively small 
- disadvantage: one graph has many possible representations (unless lists are ordered by same criterion e.g. ascending)

> [!tip] Cost Analysis
> Storage cost: O(V+E) (V list pointers, total of 2·E list elements) 
> - the larger of V,E determines the complexity 
> Cost of operations: 
> - initialisation: O(V) (initialise V lists) 
> - insert edge: O(1) (insert one vertex into list) if you don't check for duplicates 
> - find/delete edge: O(V) (need to find vertex in list)
### 3.4 Comparison of Graph Representations
![[Pasted image 20250127161754.png]]
## 4. Graph Abstract Data Type(ADT)
### 4.1 Array of Edges
```C
typedef struct GraphRep{
	Edge *edges; //array of edges
	int nv; //vertices
	int ne; //edges
	int n; //sizeof edge array which equals to V(V-1)/2
} GraphRep;
```

![[Pasted image 20250127161957.png]]
### 4.2 Adjacency Matrix
```C
typedef struct GraphRep{
	int **edges; //adjacency matrix sizeof V*V
	int nv; //vertices
	int ne; //edges
} GraphRep;
```

![[Pasted image 20250127162301.png]]
### 4.3 Adjacency List
```C
typedef struct GraphRep{
	Node **edges;
	int nv;
	int ne;
} GraphRep;

typedef struct Node{
	vertex v; //vertex is int type
	struct Node *next;
} Node;
```

![[Pasted image 20250127162643.png]]
## 5. Graph Traversal
Two strategies for graph traversal/search: depth-first, breadth-first 
- DFS follows one path to completion before considering others (深度优先搜索)
- BFS "fans-out" from the starting vertex ("spreading" subgraph) (广度优先搜索)
### 5.1 Depth-first Search (DFS)
#### Recursively(使用递归实现)
depthFirst(G,v): (传递图和访问的顶点)
1. mark v as visited (将需要访问的顶点标记为访问)
2. for each (v,w)∈edges(G) do (遍历所有与访问结点相连的结点)
	if w has not been visited then (若遍历的结点尚未被访问则访问该结点--递归直到找到终点)
	depthFirst(w) 
The recursion induces backtracking

> [!tip] Cost Analysis
>-  all vertices marked as unvisited, each vertex visited at most once ⇒ cost = O(V) 
>- visit all edges incident on visited vertices ⇒ cost = O(E)
>	- assuming an adjacency list representation
>
> Time complexity of DFS: 
> O(V+E) (adjacency list representation 邻接表实现) 
> - the larger of V,E determines the complexity 
> - For dense graphs … E ≅ $V^2$ ⇒ O(V+E) = O($V^2$) (稠密图)
> - For sparse graphs … E ≅ V ⇒ O(V+E) = O(V) (稀疏图)
>
>array-of-edges representation (边集数组实现)
>- visit all edges incident on visited vertices ⇒ cost = O(V·E) //之所以是$V*E$是因为边是总体存储在数据结构中的每遍历一个结点的访问结点需要遍历所有边
>- cost of DFS: O(V·E) 
>
>adjacency-matrix representation (邻接矩阵实现)
>- visit all edges incident on visited vertices ⇒ cost = O($V^2$) 
>- cost of DFS: O($V^2$)
#### Non-recursively (非递归实现--使用栈结构)
Pseudocode(伪代码)
```C
hasPath(G,src,dest):
	Input graph G, vertices src,dest
	Output true is there is a path from src to dest in G, false otherwise
	mark all vertices in G as unvisited
	push src onto new stack s
	found=false
	while not found and s is not empty do
		pop v from s
		mark v as visited
		if v=dest then 
			found=true
		else
			for each(v,w)in edges(g) such that w has not been visited
				push w onto s
			end for
		end if
	end while
	return found
```
### 5.2 Breadth-first Search
Basic approach to breadth-first search (BFS): 
- visit and mark current vertex 
- visit all neighbours of current vertex 
- then consider neighbours of neighbours
BFS algorithm (records visiting order, marks vertices as visited when put on queue 使用队列实现):
Pseudocode(伪代码)
```C
visited[]
findPathBFS(G,src,dest):
	Input graph G, vertices src,dest
	for all vertices v in g do
		visited[v]=-1;
	end for
	enqueue src into new queue q
	visited[src]=src;
	found=false;
	while not found and q is not empty do
		dequeue v from q
		if v=dest then
			found=true
		else 
			for each(v,w)in edges(g) such that visited[w]=-1 do
				enqueue w into q
				visited[w]=v
			end for
		end if
	end while
	if found then
		display path in dest to src order
	end if 
```
## 6. Computing Connected Components
Pseudocode(计算子树)
```C
components(G):
	Input graph G
	for all vertices v in G do
		componentOf[v]=-1 //存储子树的数组
	end for
	compID=0;
	for all vertices v in G do
		if componentOf[v]=-1 then
			dfsComponents(G,v,compID); //存放所有子树的结点
			compID++;//子树编号自增
		end if
	end for
dfsComponents(G,v,id):
	componentOf[v]=id;
	for all vertives w adjacent to v do
		if componentOf[w]=-1 then
			dfsComponents(G,w,id);
		end if
	end for
```
## 7. Hamiltonian and Euler Paths
### 7.1 Hamiltonian Problem
Hamiltonian path problem: (汉密尔顿路径 找到一条经过所有顶点仅一次的路径)
- find a path connecting two vertices v,w in graph G 
- such that the path includes each vertex exactly once 
If v = w, then we have a Hamiltonian circuit (汉密尔顿环路)
Simple to state, but difficult to solve (NP-complete)
Pseudocode
```C
visited[]

hasHamiltonianPath(G,src,dest):
	for all vertices v in G do
		visited[v]=false;
	end for
	return hamiltonR(G,src,dest,#vertices(G)-1)

hamiltonR(G,v,dest,d):
	Input G graph
		  v current vertex considered
		  dest destination vertex
		  d distance "remaining" until path found //答案路径的剩余边数
	if v=dest then
		if d=0 then return true else return false
	else
		mark v as visited
		for each neighbour w of v in G do
			if w has not been visited then
				if hamiltonR(G,w,dest,d-1) then
					return true
				end if
			end if
		end for
	end if
	mark v as unvisited
	return false
```
### 7.2 Euler Problem
Euler path problem: 
- find a path connecting two vertices v,w in graph G 
- such that the path includes each edge exactly once (note: the path does not have to be simple ⇒ can visit vertices more than once)
Pseudocode
```C
hasEulerPath(G,src,dest):
	Input graph G, vertices src,dest
	Output true if G has Euler path from src to dest
		false otherwise
	if src!=dest then
		if degree(G,src) or degree(G,dest) is even then
			return false
		end if
	else if degree(G,src) is odd then
		return false
	end if
	for all vertices v in G do
		if v!=src and v!=dest and degree(G,v) is odd then 
			return false
		end if
	end for
	return true
```
## 8. Directed Graphs
In our previous discussion of graphs: 
- an edge indicates a relationship between two vertices 
- an edge indicates nothing more than a relationship 
In many real-world applications of graphs: 
- edges are directional (v → w ≠ w → v) edges have a weight (cost to go from v → w)
## 9. Reachability(图的可达性)
```C
make tc[][] a copy of edges[][]
for all i in vertices(G) do
	for all s in vertices(G) do
		for all t in vertices(G) do
			if tc[s][i] and tc[i][t]=1 then
				tc[s][t]=1
			end if
		end for
	end for
end for
```
This is known as Warshall's algorithm
## 10. Weighted Graph
Graphs so far have considered 
- edge = an association between two vertices/nodes 
- may be a precedence in the association (directed) 
Some applications require us to consider 
- a cost or weight of an association 
- modelled by assigning values to edges (e.g. positive reals) 
Weights can be used in both directed and undirected graphs.

> [!tip] Weighted Graph Representation
> Weights can easily be added to: 
> - adjacency matrix representation (0/1 → int or float) 
> - adjacency lists representation (add int/float to list node) Both representations work whether edges are directed or not.
> 
## 11. Minimum Spanning Trees(最小生成树)
Reminder: Spanning tree ST of graph G=(V,E) (经过该图的所有顶点)
- spanning = all vertices, tree = no cycles 
	- ST is a subgraph of G (G'=(V,E') where E' ⊆ E) 
	- ST is connected and acyclic 
Minimum spanning tree MST of graph G 
- MST is a spanning tree of G 
- sum of edge weights is no larger than any other ST
### 11.1 Kruskal's Algorithm(克鲁斯卡尔算法)
Pseudocode:
```C
KruskalMST(G):
	Input graph G with n nodes
	Output a minimum spanning tree of G
	MST=empty graph
	sort edges(G) by weight
	for each e in sortedEdgeList do //循环寻找整个图中的最小边并且去环
		MST=MST U {e}
		if MST has a cycle then
			MST=MST\{e}
		end if 
		if MST has n-1 edges then 
			return MST
		end if
	end for
```
### 11.2 Prim's Algorithm(普利姆算法)
Another approach to computing MST for graph G=(V,E): 
1. start from any vertex v and empty MST 
2. choose edge not already in MST to add to MST 
	1. must be incident on a vertex s already connected to v in MST
	2. must be incident on a vertex t not already connected to v in MST 
	3. must have minimal weight of all such edges 
3. repeat until MST covers all vertices
## 12. Single-source Shortest Path(SSSP 单源最短路径)
Given: weighted digraph G, source vertex s 
Result: shortest paths from s to all other vertices 
- dist[] V-indexed array of cost of shortest path from s 
- pred[] V-indexed array of predecessor in shortest path from s
Pseudocode:
```C
dist[] //array of cost of shortest path from s
pred[] //array of predecessor(先驱结点) in shortest path from s
dijkstraSSSP(G,source):
	Input graph G, source node
	initialise dist[] to all, except dist[source]=0;
	intialise pred[] to all -1;
	vSet=all vertices of G
	while vSet!=empty do
		find s in vSet with minimum dist[s]
		for each (s,t,w) in edges(G) do
			relax along(s,t,w)
		end for
		vSet=vSet\{s}
	end while
```