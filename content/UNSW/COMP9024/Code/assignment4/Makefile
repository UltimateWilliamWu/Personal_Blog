CC = gcc
CCFLAGS = -Wall -Werror -std=c11

trails : trails.o WGraph.o Queue.o
	$(CC) -o trails trails.o WGraph.o Queue.o

treeLab : treeLab.o BST.o
	$(CC) -o treeLab treeLab.o BST.o

RBTree : RBTree.o RBTester.o
	$(CC) -o rbt RBTester.o RBTree.o

treeLab.o : treeLab.c BST.h
	$(CC) $(CCFLAGS) -c treeLab.c

BST.o : BST.c BST.h
	$(CC) $(CCFLAGS) -c BST.c

RBTester.o : RBTester.c RBTree.h
	$(CC) $(CCFLAGS) -c RBTester.c

RBTree.o : RBTree.c RBTree.h
	$(CC) $(CCFLAGS) -c RBTree.c

trails.o : trails.c WGraph.h Queue.h
	$(CC) $(CCFLAGS) -c trails.c WGraph.h Queue.h

WGraph.o : WGraph.c WGraph.h
	$(CC) $(CCFLAGS) -c WGraph.c

Queue.o : Queue.c Queue.h
	$(CC) $(CCFLAGS) -c Queue.c

clean:
	rm -f *.o
