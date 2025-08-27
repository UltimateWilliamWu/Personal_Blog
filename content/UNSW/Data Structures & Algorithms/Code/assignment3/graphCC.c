// Graph ADT
// Adjacency Matrix Representation ... COMP9024 25T0
#include "graphCC.h"
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct GraphRep {
   int  **edges;   // adjacency matrix
   int    nV;      // #vertices
   int    nE;      // #edges
   int nC;  // # connected components
   int *cc; /* which component each vertex is contained in
               i.e. array [0..nV-1] of 0..nC-1 */
} GraphRep;

Graph newGraph(int V) {
   assert(V >= 0);
   int i;

   Graph g = malloc(sizeof(GraphRep));
   assert(g != NULL);
   g->nV = V;
   g->nE = 0;
   g->nC=V;
   // allocate memory for each row
   g->edges = malloc(V * sizeof(int *));
   assert(g->edges != NULL);
   // allocate memory for each column and initialise with 0
   for (i = 0; i < V; i++) {
      g->edges[i] = calloc(V, sizeof(int));
      assert(g->edges[i] != NULL);
   }

   g->cc=malloc(V*sizeof(int*));
   for(i=0;i<V;i++){
      g->cc[i]=1;
      for(int j=0;j<V;j++){
        g->edges[i][j]=0;
      }
   }
   return g;
}

int numOfVertices(Graph g) {
   return g->nV;
}

// check if vertex is valid in a graph
bool validV(Graph g, Vertex v) {
   return (g != NULL && v >= 0 && v < g->nV);
}

void insertEdge(Graph g, Edge e) {
   assert(g != NULL && validV(g,e.v) && validV(g,e.w));

   if (!g->edges[e.v][e.w]) {  // edge e not in graph
      g->edges[e.v][e.w] = 1;
      g->edges[e.w][e.v] = 1;
      g->nE++;
   }
}

void removeEdge(Graph g, Edge e) {
   assert(g != NULL && validV(g,e.v) && validV(g,e.w));

   if (g->edges[e.v][e.w]) {   // edge e in graph
      g->edges[e.v][e.w] = 0;
      g->edges[e.w][e.v] = 0;
      g->nE--;
   }
}

bool adjacent(Graph g, Vertex v, Vertex w) {
   assert(g != NULL && validV(g,v) && validV(g,w));

   return (g->edges[v][w] != 0);
}

void showGraph(Graph g) {
    assert(g != NULL);
    int i, j;

    printf("Number of vertices: %d\n", g->nV);
    printf("Number of edges: %d\n", g->nE);
    for (i = 0; i < g->nV; i++)
       for (j = i+1; j < g->nV; j++)
	  if (g->edges[i][j])
	      printf("Edge %d - %d\n", i, j);
}

void freeGraph(Graph g) {
   assert(g != NULL);

   int i;
   for (i = 0; i < g->nV; i++)
      free(g->edges[i]);
   free(g->edges);
   free(g);
}

void dfsComponents(Graph g, int v, int id) {
   g->cc[v] = id;
   Vertex w;
   for (w = 0; w < numOfVertices(g); w++)
      if (adjacent(g, v, w) && g->cc[w] == -1)
	 dfsComponents(g, w, id);
}

// computes the connected component array
// and returns the number of connected components
void components(Graph g) {
   Vertex v;
   int nV = numOfVertices(g);
   for (v = 0; v < nV; v++)
      g->cc[v] = -1;

   int compID = 0;
   for (v = 0; v < nV; v++) {
      if (g->cc[v] == -1) {
	 dfsComponents(g, v, compID);
	 compID++;
      }
   }
   //return compID;
}

void showComponents(Graph g){
   printf("Connected components: \n");
   components(g);
   Vertex v;
      for (v = 0; v < g->nV; v++){
         if(v==g->nV-1){
            printf("%d",g->cc[v]);
         }else{
            printf("%d, ", g->cc[v]);
         }
      }	    
}