// Prim's algorithm to compute MST
#include "Set.h"
#include "WGraph.h"
#include <limits.h>
#include <stdlib.h>
#include <stdio.h>

void prim(Graph g, int nV, Vertex startingVertex) {
   Graph mst = newGraph(nV); // Create a new null mst
   Set usedV = newSet();     // Stored visited vertices
   Vertex v, w;
   Edge bestEdge;
   int weight, minWeight;

   addToSet(usedV, startingVertex); // Put the startingVertex into the visited set

   /* NEEDS TO BE COMPLETED */
   while (sizeSet(usedV) < nV) { // visit all the vertices
      minWeight = INT_MAX; // using INT_MAX to initialize the weight

      // travel all the visited vertex，find the minimum weight edge to unvisited vertex
      for (v = 0; v < nV; v++) {
         if (elementOfSet(usedV, v)) {
            for (w = 0; w < nV; w++) {
               // find unvisited vertex and weight is smaller than current smallest weight
               if (!elementOfSet(usedV, w) && adjacent(g, v, w) > 0) {
                  weight = adjacent(g,v,w);
                  if (weight < minWeight) {
                     bestEdge.v = v;
                     bestEdge.w = w;
                     minWeight = weight;
                  }
               }
            }
            bestEdge.weight=minWeight;
         }
      }

      // if couldn't find valid edge means the graph is not connected
      if (bestEdge.weight == INT_MAX) {
         fprintf(stderr, "Error: Graph is not connected.\n");
         freeSet(usedV);
         freeGraph(mst);
         return;
      }

      // find the best edge and add to MST
      insertEdge(mst, bestEdge);
      printf("Edge with weight %d added.\n",bestEdge.weight);

      // mark the new vertex as used
      addToSet(usedV, bestEdge.w);
   }
   printf("\n");
   showGraph(mst); // show the mst
   freeSet(usedV);
   freeGraph(mst);
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
      v = e.v;        // add edge in both directions
      e.v = e.w;
      e.w = v;
      insertEdge(g, e);
      printf("Enter an edge (from): ");
   }
   while (getchar() != '\n');       // clears the input stream
   printf("Done.\n");
   printf("Enter the starting vertex: \n");
   scanf("%d", &v);
   /* NEEDS TO BE COMPLETED */
   if (v < 0 || v >= nV) {
      fprintf(stderr, "Error: Invalid starting vertex.\n");
      freeGraph(g);
      return 1;
   }
   prim(g, nV, v);
   freeGraph(g);
   return 0;
}
