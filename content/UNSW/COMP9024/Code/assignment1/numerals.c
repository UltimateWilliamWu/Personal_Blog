// convert positive integer to different numeral base ... COMP9024 25T0

#include <stdio.h>
#include "stack.h"

void numeralConversion(int n, int k) {
   StackInit();
   while (n > 0) {
      StackPush(n % k);
      n = n / k;
   }
   while (!StackIsEmpty()) {
      printf("%d", StackPop());
   }
   putchar('\n');
}

int main(void) {
   numeralConversion(13, 2);
   return 0;
} 
