#include<stdio.h>
#include<stdlib.h>
#include"charStack.h"

// set up empty stack
void StackInit(stack *s){
    s->base = (char*)malloc(MAXITEMS * sizeof(char));
    if (!s->base) exit(0);  
    for (int n = 0; n < s->top; n++) {
        s->base[n] = 0;
    }
    s->top = -1;
    s->stacksize = MAXITEMS;
}

// check whether stack is empty
int  StackIsEmpty(stack *s){
    if (s->top!=0)
    {
        printf("Stack is not empty!");
        return 1;
    }else{
        printf("Stack is empty!");
        return 0;
    }
    
}

// insert char on top of stack
stack* StackPush(char c,stack *s){
    s->base[s->top]=c;
    s->top++;
    return s;
}  

// remove char from top of stack
char StackPop(stack *s){
    char c=s->base[s->top];
    return c;
}       