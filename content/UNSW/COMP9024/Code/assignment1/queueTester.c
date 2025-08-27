// Character Stack ADO tester

#include <stdio.h>
#include "queue.h"

int main(void) {
   char str[MAXITEMS] = "string";
   int i = 0;
   
   QueueInit();
   while (str[i] != '\0') {
      QueueEnqueue(str[i]);
      i++;
   }
   while (!QueueIsEmpty()) {
      char c = QueueDequeue();
      putchar(c);
   }
   putchar('\n');
   return 0;
}