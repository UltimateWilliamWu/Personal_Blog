#include<stdio.h>
#include"WGraph.h"
#include<assert.h>
#include<stdlib.h>

typedef struct {
    int index;
    int inboundLinks;
    int score;
} PageInfo;

int numPages;

Graph inputNumpage(){
    Edge e;
    int webpage,linkwp;
    printf("Enter the number of webpages:");
    scanf("%d",&numPages);
    Graph g = newGraph(numPages);
    while(1){
        printf("Enter a webpage:");
        if(scanf("%d", &webpage)!=1){
            printf("Done.\n");
            break;
        }
        printf("Enter a link on webpage %d:",webpage);
        if(scanf("%d", &linkwp)!=1){
            printf("Done.\n");
            break;
        }
        e.v=webpage;e.w=linkwp;e.weight=1;
        insertEdge(g,e);
    }
    return g;
}

int* initialArray(){
    int* count=malloc(numPages*sizeof(int));
    assert(count != NULL);
    for(int i=0;i<numPages;i++){
        count[i]=0;
    }
    return count;
}

void boundCount(Graph g,int* inbound,int* outbound){
    for (int i = 0; i < numPages; i++) {
        for(int j=0;j<numPages;j++){
            if(adjacent(g,i,j)==1){
                inbound[j]++;
                outbound[i]++;
            }
        }
    }
}

// comparing function，using for descending inboundlinks
int compareDesc(const void *a, const void *b) {
    const PageInfo *page1 = (const PageInfo *)a;
    const PageInfo *page2 = (const PageInfo *)b;

    // descending inboundlinks
    if (page1->inboundLinks != page2->inboundLinks) {
        return page2->inboundLinks - page1->inboundLinks;//if result is negative, then swap. if result is positive then not swap
    }

    // when the inboundlinks is the same, descending scores
    if (page1->score != page2->score) {
        return page2->score - page1->score;
    }

    // when the inboundlinks and scores are both the same, follow the index
    return page1->index - page2->index;
}

// show output
void sortArrayWithIndices(int *inbound, int *outbound, Graph g) {
    PageInfo *pages = malloc(numPages * sizeof(PageInfo));
    assert(pages != NULL);

    // create index arrays
    for (int i = 0; i < numPages; i++) {
        pages[i].index = i;
        pages[i].inboundLinks = inbound[i];
        pages[i].score = 0;

        // calculate scores
        for (int j = 0; j < numPages; j++) {
            if (adjacent(g,j,i) == 1) {
                pages[i].score += outbound[j];
            }
        }
    }

    // using qsort to descending the order
    qsort(pages, numPages, sizeof(PageInfo), compareDesc);

    printf("\nWebpage ranking:\n");
    for (int i = 0; i < numPages; i++) {
        printf("%d has %d inbound links and scores %d on inbound links. \n", pages[i].index,pages[i].inboundLinks,pages[i].score);
    }

    // release memory
    free(pages);
}

int main(void){
    Graph g = inputNumpage();
    int* boundin=initialArray();
    int* boundout=initialArray();
    boundCount(g,boundin,boundout);
    sortArrayWithIndices(boundin,boundout,g);
    freeGraph(g);
    return 0;
}