// Character Stack ADO tester

#include <stdio.h>
#include "charStack.h"
#include<stdlib.h>

#define STRLEN 7

int main(void) {
   stack *str=(stack*)malloc(sizeof(stack));
   
   StackInit(str);
   
   putchar('\n');
   return 0;
}