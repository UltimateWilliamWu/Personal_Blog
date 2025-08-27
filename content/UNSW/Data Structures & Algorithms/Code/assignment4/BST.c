// Binary Search Tree ADT implementation ... COMP9024 25T0

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include "BST.h"

#define RANDOM_ROOT_INSERT (rand() % 10 < 4)   // 40% chance

#define data(tree)  ((tree)->data)
#define left(tree)  ((tree)->left)
#define right(tree) ((tree)->right)

typedef struct Node {
   Item data;
   Tree left, right;
} Node;

// make a new node containing data
Tree newNode(Item it) {
   Tree new = malloc(sizeof(Node));
   assert(new != NULL);
   data(new) = it;
   left(new) = right(new) = NULL;
   return new;
}

// create a new empty Tree
Tree newTree() {
   return NULL;
}

// free memory associated with Tree
void freeTree(Tree t) {
   if (t != NULL) {
      freeTree(left(t));
      freeTree(right(t));
      free(t);
   }
}

// compute height of Tree
int TreeHeight(Tree t) {
   if (t == NULL) {
      return -1;
   } else {
      int lheight = 1 + TreeHeight(left(t));
      int rheight = 1 + TreeHeight(right(t));
      if (lheight > rheight)
	 return lheight;
      else
	 return rheight;
   }
}

// count #nodes in Tree
int TreeNumNodes(Tree t) {
   if (t == NULL)
      return 0;
   else
      return 1 + TreeNumNodes(left(t)) + TreeNumNodes(right(t));
}

// check whether a key is in a Tree
bool TreeSearch(Tree t, Item it) {
   if (t == NULL)
      return false;
   else if (it < data(t))
      return TreeSearch(left(t), it);
   else if (it > data(t))
      return TreeSearch(right(t), it);
   else                                 // it == data(t)
      return true;
}

// insert a new item into a Tree
Tree TreeInsert(Tree t, Item it) {
   if (t == NULL)
      t = newNode(it);
   else if (it < data(t))
      left(t) = TreeInsert(left(t), it);
   else if (it > data(t))
      right(t) = TreeInsert(right(t), it);
   return t;
}

Tree joinTrees(Tree t1, Tree t2) {
   if (t1 == NULL)
      return t2;
   else if (t2 == NULL)
      return t1;
   else {
      Tree curr = t2;
      Tree parent = NULL;
      while (left(curr) != NULL) {    // find min element in t2
	 parent = curr;
	 curr = left(curr);
      }
      if (parent != NULL) {
	 left(parent) = right(curr);  // unlink min element from parent
	 right(curr) = t2;
      }
      left(curr) = t1;
      return curr;                    // min element is new root
   }
}

// delete an item from a Tree
Tree TreeDelete(Tree t, Item it) {
   if (t != NULL) {
      if (it < data(t))
	 left(t) = TreeDelete(left(t), it);
      else if (it > data(t))
	 right(t) = TreeDelete(right(t), it);
      else {
	 Tree new;
	 if (left(t) == NULL && right(t) == NULL) 
	    new = NULL;
	 else if (left(t) == NULL)    // if only right subtree, make it the new root
	    new = right(t);
	 else if (right(t) == NULL)   // if only left subtree, make it the new root
	    new = left(t);
	 else                         // left(t) != NULL and right(t) != NULL
	    new = joinTrees(left(t), right(t));
	 free(t);
	 t = new;
      }
   }
   return t;
}

Tree rotateRight(Tree n1) {
   if (n1 == NULL || left(n1) == NULL)
      return n1;
   Tree n2 = left(n1);
   left(n1) = right(n2);
   right(n2) = n1;
   return n2;
}

Tree rotateLeft(Tree n2) {
   if (n2 == NULL || right(n2) == NULL)
      return n2;
   Tree n1 = right(n2);
   right(n2) = left(n1);
   left(n1) = n2;
   return n1;
}

Tree insertAtRoot(Tree t, Item it) { 
   if (t == NULL) {
      t = newNode(it);
   } else if (it < data(t)) {
      left(t) = insertAtRoot(left(t), it);
      t = rotateRight(t);
   } else if (it > data(t)) {
      right(t) = insertAtRoot(right(t), it);
      t = rotateLeft(t);
   }
   return t;
}

Tree insertRandom(Tree t, Item it) { 
   if (t == NULL)
      t = newNode(it);
   if (RANDOM_ROOT_INSERT)
      return insertAtRoot(t, it);
   else
      return TreeInsert(t, it);
}

Tree insertAVL(Tree t, Item it) {
   if (t == NULL)
      return newNode(it);
   if (it == data(t))
      return t;

   if (it < data(t))
      left(t) = insertAVL(left(t), it);
   else
      right(t) = insertAVL(right(t), it);

   int hL = TreeHeight(left(t));
   int hR = TreeHeight(right(t));
   if ((hL - hR) > 1) {
      if (it > data(left(t))) {
         left(t) = rotateLeft(left(t));
      }
      t = rotateRight(t);
   } else if ((hR - hL) > 1) {
      if (it < data(right(t))) {
	 right(t) = rotateRight(right(t));
      }
      t = rotateLeft(t);
   }

   return t;
}

Tree insertSplay(Tree t, Item it) {
   if (t == NULL)
      return newNode(it);
   if (it == data(t))
      return t;

   if (it < data(t)) {
      if (left(t) == NULL) {
	 left(t) = newNode(it);
      } else if (it < data(left(t))) {
	 left(left(t)) = insertSplay(left(left(t)), it);
	 t = rotateRight(t);
      } else if (it > data(left(t))) {
	 right(left(t)) = insertSplay(right(left(t)), it);
	 left(t) = rotateLeft(left(t));
      }
      return rotateRight(t);
   } else {
      if (right(t) == NULL) {
	 right(t) = newNode(it);
      } else if (it < data(right(t))) {
	 left(right(t)) = insertSplay(left(right(t)), it);
	 right(t) = rotateRight(right(t));
      } else if (it > data(right(t))) {
	 right(right(t)) = insertSplay(right(right(t)), it);
	 t = rotateLeft(t);
      }
      return rotateLeft(t);
   }
}

Tree partition(Tree t, int i) {
   if (t != NULL) {
      assert(0 <= i && i < TreeNumNodes(t));
      int m = TreeNumNodes(left(t));
      if (i < m) {
	 left(t) = partition(left(t), i);
	 t = rotateRight(t);
      } else if (i > m) {
	 right(t) = partition(right(t), i-m-1);
	 t = rotateLeft(t);
      }
   }
   return t;
}

Tree rebalance(Tree t) {
   int n = TreeNumNodes(t);

   if (n >= 3) {
      t = partition(t, n/2);           // put node with median key at root
      left(t) = rebalance(left(t));    // then rebalance each subtree
      right(t) = rebalance(right(t));
   }
   return t;
}


// insert all the nodes to the AVL tree
Tree insertAllAVL(Tree t, Tree s) {
   if (s == NULL)
      return t;
   t = insertAllAVL(t, left(s));
   t = insertAVL(t, data(s));
   t = insertAllAVL(t, right(s));
   return t;
}

Tree deleteAVL(Tree t, Item it) {
   if (t == NULL)
      return t;

   if (it < data(t))
      left(t) = deleteAVL(left(t), it);
   else if (it > data(t))
      right(t) = deleteAVL(right(t), it);
   else {  // find the delete node
      if (left(t) == NULL || right(t) == NULL) {
         Tree temp = (left(t) != NULL) ? left(t) : right(t);
         free(t);
         t = temp;
      } else {
         /* When the node has two children:
            Use the right subtree as the new tree,
            then insert all nodes from the original left subtree
            into the new tree.
            This approach results in the following AVL tree structure:
         */
         Tree oldLeft = left(t);  // Save the left subtree of the node to be deleted.
         Tree temp = t;
         t = right(t);            // The new tree is the right subtree.
         free(temp);
         t = insertAllAVL(t, oldLeft);  // Insert all nodes from the left subtree into the new tree.
      }
   }

   if (t == NULL)
      return t;

   /* Balance correction: adjust the AVL balance using the height difference between the left and right subtrees */
   int hL = TreeHeight(left(t));
   int hR = TreeHeight(right(t));
   int balance = hL - hR;

   if (balance > 1) {  // Left subtree is too high.
      if (TreeHeight(left(left(t))) >= TreeHeight(right(left(t))))
         t = rotateRight(t);         // Left-Left case: perform a single right rotation.
      else {
         left(t) = rotateLeft(left(t));  // Left-Right case: first perform a left rotation on the left subtree,
         t = rotateRight(t);
      }
   } else if (balance < -1) {  // Right subtree is too high.
      if (TreeHeight(right(right(t))) >= TreeHeight(left(right(t))))
         t = rotateLeft(t);          // Right-Right case: perform a single left rotation.
      else {
         right(t) = rotateRight(right(t)); // Right-Left case: first perform a right rotation on the right subtree,
         t = rotateLeft(t);
      }
   }
   
   return t;
}


// display tree

void showTreeR(Tree t, int depth) {
   if (t != NULL) {
      showTreeR(right(t), depth+1);
      int i;
      for (i = 0; i < depth; i++)
	 putchar('\t');            // TAB character
      printf("%d\n", data(t));
      showTreeR(left(t), depth+1);
   }
}

void showTree(Tree t) {
   showTreeR(t, 0);
}
