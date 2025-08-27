#include<stdio.h>
#include"stack.h"
#include<assert.h>
typedef struct 
{
    int array[MAXITEMS];
    int top;
} stack;

static stack sq;

void StackInit(){
    sq.top=-1;
};     // set up empty stack
int  StackIsEmpty(){
    return(sq.top<0);
};  // check whether stack is empty
void StackPush(int n){
    assert(sq.top<MAXITEMS-1);
    sq.top++;
    sq.array[sq.top]=n;
};  // insert int on top of stack
int  StackPop(){
    assert(sq.top>-1);
    int result= sq.array[sq.top];
    sq.top--;
    return result;
};      // remove int from top of stack