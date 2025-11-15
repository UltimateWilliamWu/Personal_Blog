---
tags:
  - LectureNotes
---
## 1. Searching
Cost of searching:
![[Pasted image 20250128153444.png]]
- O(n) for linear scan
- O(log n) binary search, search trees(二叉树，搜索树)
## 2. Tree Data Structures
Trees are connected graphs 
- consisting of nodes and edges (called links), with no cycles (no "up-links") 
- each node contains a data value (or key+data) 
- each node has links to ≤ k other child nodes (k=2 below)
> [!tip] Special kinds of tree
> - m-ary tree: each internal node has exactly m children (每个父结点有m个子结点)
> - Ordered tree: all left values < root, all right values > root (排序树)
> - Balanced tree: has ≅minimal height for a given number of nodes (平衡树) 
> - Degenerate tree: has ≅maximal height for a given number of nodes 
### 2.1 Binary Search Trees（二叉搜索树）
Level of node = path length from root to node 
Height (or: depth) of tree = max path length from root to leaf
Height-balanced tree: ∀ nodes: height(left subtree) = height(right subtree) ± 1 
Time complexity of tree algorithms is typically O(height)
![[Pasted image 20250211230845.png]]
### 2.2 Balanced BST（平衡二叉搜索树）
Left rotation 
- move right child to root; rearrange links to retain order 
Right rotation 
- move left child to root; rearrange links to retain order 
Insertion at root 
- each new item is added as the new root node
![[Pasted image 20250211231115.png]]
### 2.3 Splay Trees（延伸树）
Cases for splay tree double-rotations: 
- case 1: grandchild is left-child of left-child ⇒ double right rotation from top 
- case 2: grandchild is right-child of left-child ⇒ rotate left then rotate right
- case 3: grandchild is left-child of right-child ⇒ rotate right then rotate left
- case 4: grandchild is right-child of right-child ⇒ double left rotation from top
### 2.4 AVL Trees（严格二叉平衡树）
A tree is unbalanced when: abs(height(left)-height(right)) > 1 （左右子树高度差不大于1）
This can be repaired by at most two rotations: 
- if left subtree too deep … 
	- if data inserted in left-right grandchild ⇒ left-rotate left subtree 
	- rotate right 
- if right subtree too deep … 
	- if data inserted in right-left grandchild ⇒ right-rotate right subtree 
	- rotate left
![[Pasted image 20250211232055.png]]
### 2.5 2-3-4 Trees
![[Pasted image 20250211232123.png]]
2-3-4 tree searching cost analysis: 
- as for other trees, worst case determined by height h 
- 2-3-4 trees are always balanced ⇒ height is O(log n) 
- worst case for height: all nodes are 2-nodes same case as for balanced BSTs, i.e. h ≅ log2 n 
- best case for height: all nodes are 4-nodes balanced tree with branching factor 4, i.e. h ≅ log4 n
### 2.6 Red-Black Trees（红黑树）
为什么使用红黑树？
1. 严格二叉树的旋转操作过于频繁
2. 普通二叉树最差情况是链表，搜索复杂度高
Definition of a red-black tree 
- a BST in which each node is marked red or black 
- no two red nodes appear consecutively on any path 
- a red node corresponds to a 2-3-4 sibling of its parent 
- a black node corresponds to a 2-3-4 child of its parent 
	- if no parent (= root) → also black 
Balanced red-black tree 
- all paths from root to leaf have same number of black nodes