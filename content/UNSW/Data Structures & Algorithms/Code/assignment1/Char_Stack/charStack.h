// Character Stack ADO header file

#define MAXITEMS 10

typedef struct{
    char* base;
    int   top;
    int  stacksize;
}stack;

void StackInit(stack*);      // set up empty stack
int  StackIsEmpty(stack* s);   // check whether stack is empty
stack * StackPush(char c,stack* s);  // insert char on top of stack
char StackPop(stack* s);       // remove char from top of stack