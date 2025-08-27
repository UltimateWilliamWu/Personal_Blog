CC = gcc
CCFLAGS = -Wall -Werror -std=c11

connectedComponents: connectedComponents.o graphCC.o
	$(CC) $(CCFLAGS) -o connectedComponents connectedComponents.o graphCC.o

connectedComponents.o: connectedComponents.c graphCC.h
	$(CC) $(CCFLAGS) -c connectedComponents.c

graphCC.o: graphCC.c graphCC.h
	$(CC) $(CCFLAGS) -c graphCC.c

pageRank: pageRank.o WGraph.o
	$(CC) $(CCFLAGS) -o pageRank pageRank.o WGraph.o

pageRank.o: pageRank.c WGraph.h
	$(CC) $(CCFLAGS) -c pageRank.c

WGraph.o: WGraph.c WGraph.h
	$(CC) $(CCFLAGS) -c WGraph.c

prim: prim.o Set.o WGraph.o
	$(CC) $(CCFLAGS) -o prim prim.o Set.o WGraph.o

prim.o: prim.c Set.h WGraph.h
	$(CC) $(CCFLAGS) -c prim.c

Set.o: Set.c Set.h
	$(CC) $(CCFLAGS) -c Set.c

clean:
	rm -f *.o
