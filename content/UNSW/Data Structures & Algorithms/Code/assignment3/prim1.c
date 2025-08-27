// Prim's algorithm to compute MST
#include "Set.h"
#include "WGraph.h"
#include <limits.h>
#include <stdlib.h>
#include <stdio.h>
typedef struct GraphRep {
   int  **edges;   // adjacency matrix
   int    nV;      // #vertices
   int    nE;      // #edges
} GraphRep;

void prim(Graph g, int nV, Vertex startingVertex) {
   Graph mst = newGraph(nV);
   Set usedV = newSet();
   Vertex v, w;
   Edge bestEdge;
   int weight, minWeight;
   addToSet(usedV, startingVertex);
   /* NEEDS TO BE COMPLETED */
   //1.Find the minimum weight of specified vertex
   for(int i=0;i<g->nV;i++){
      weight=adjacent(g,startingVertex,i);
      if(!minWeight){
         minWeight=weight;
      }else{
         if(minWeight>weight){
            minWeight=weight;
            w=i;            
         }
      } 
   }
   v=startingVertex;
   addToSet(usedV,w);
   for(int i=0;i<g->nV;i++){
      if(elementOfSet(usedV,i)){
         continue;
      }
      for(int j=0;j<g->nV;j++){
         weight=adjacent(g,i,j);
         if(!minWeight){
            minWeight=weight;
         }else{
            if(minWeight>weight){
            minWeight=weight;
            w=i;            
            }
         } 
      }
   }


   bestEdge.v=v;
   bestEdge.w=w;
   bestEdge.weight=minWeight;
   insertEdge(mst,bestEdge);


   printf("Edge with weight %d added.\n",minWeight);
   printf("Edge %d-%d:%d",v,w,minWeight);
}



int main(void) {
   int nV;
   Edge e;
   Vertex v;

   printf("Enter the number of vertices: ");
   scanf("%d", &nV);
   Graph g = newGraph(nV);

   printf("Enter an edge (from): ");
   while (scanf("%d", &e.v) == 1) {
      printf("Enter an edge (to): ");
      scanf("%d", &e.w);
      printf("Enter the weight: ");
      scanf("%d", &e.weight);
      insertEdge(g, e);
      v = e.v;                          // add edge in both directions
      e.v = e.w;
      e.w = v;
      insertEdge(g, e);
      printf("Enter an edge (from): ");
   }
   while (getchar() != '\n');           // clears the input stream
   printf("Done.\n");
   printf("Enter the starting vertex: ");
   scanf("%d", &v);


   /* NEEDS TO BE COMPLETED */
   prim(g,nV,v);
   
   return 0;
}