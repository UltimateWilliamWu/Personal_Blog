// Graph ADT tester ... COMP9024 25T0
#include "Graph.h"
#include <stdio.h>
#define NODES 1000

typedef struct GraphRep {
   int  **edges;   // adjacency matrix
   int    nV;      // #vertices
   int    nE;      // #edges
} GraphRep;

Graph inputGraph(){
    Edge e;
    int numOfVertex,from,to;
    printf("Enter the number of vertices:");
    scanf("%d",&numOfVertex);
    Graph g = newGraph(numOfVertex);
    while(1){
        printf("Enter an edge(from):");
        if(scanf("%d", &from)!=1){
            printf("Done.");
            break;
        }
        printf("Enter an edge(to):");
        if(scanf("%d", &to)!=1){
            printf("Done.");
            break;
        }
        e.v=from;e.w=to;
        insertEdge(g,e);
   }
   return g;
}

void printDegree(GraphRep* g){
   int count=0;
   for(int i=0;i< g->nV;i++){
        for(int j=0;j< g->nV;j++){
          if (g->edges[i][j]){
                count++;
            }  
        }
        printf("\nDegree of node %d: %d",i,count);
        count=0;
   }
   printf("\n");
}

void printCliques(GraphRep* g){
    printf("3-cliques:\n");
    for(int i=0;i<g->nV;i++){
        for(int j=i+1;j<g->nV;j++){
            if(g->edges[i][j]){
                for(int k=j+1;k<g->nV;k++){
                    if(g->edges[j][k]&&g->edges[k][i]){
                        printf("%d-%d-%d\n",i,j,k);
                    }
                }
            }
        }
    }
}

void printDensity(GraphRep* g){
    int edge=g->nE;
    int vertex=g->nV;
    double result=(2.0*edge)/(vertex*(vertex-1.0));
    printf("Density:%.3f\n",result);
}

int main(void) {
    Graph g = inputGraph();
    printDegree(g);
    printCliques(g);
    printDensity(g);
    freeGraph(g);
    return 0;
}
