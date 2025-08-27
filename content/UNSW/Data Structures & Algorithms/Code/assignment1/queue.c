#include<stdio.h>
#include"queue.h"
#include<stdlib.h>

typedef struct cqueue{
    char    base[MAXITEMS]; 
    int     front;
    int     rear;
}cqueue;     

static cqueue cq;

// set up empty queue
void QueueInit(){
    cq.front=0;
    cq.rear=0;
}

// check whether queue is empty
int  QueueIsEmpty(){
    if (cq.rear==cq.front) return 1;
    else return 0;
}

// insert char at end of queue
void QueueEnqueue(char c){
    cq.base[cq.rear]=c;
    cq.rear=(cq.rear+1) % MAXITEMS; 
}

// remove char from front of queue
char QueueDequeue(){
    char e= cq.base[cq.front];
    cq.front=(cq.front+1) % MAXITEMS; 
    return e;
}    