---
tags:
  - Assignment
---
1. Find all of the problems and solve it
```C
/**
 * Each of the functions f1() to f8() below contains
 * a common memory mistake that results in either
 * a run-time error or "undefined behaviour".
 * 
 * First identify each mistake, then correct it.  Fixing the 
 * code will require adding, modifying, moving, or removing 
 * one line of code in each of the 8 functions.
 * 
 * Once corrected, the code should compile without warnings,
 * run without error, and not leak any memory.
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/* swap the values of two float variables */
void swap(float *p, float *q) {
   float temp = *p;
   *p = *q;
   *q = temp;
}

/* copy the values of float array a[] to b[] */
void copy(float a[], float b[], int size) {
   int i;
   for (i = 0; i < size; i++) {
      b[i] = a[i];
   }
}

/* print all the values of a dynamic float array */
void print(float *b, int size) {
   int i;
   for (i = 0; i < size; i++) {
      printf("%5.2f ", b[i]);
   }
   putchar('\n');
   free(b);
}

/* DO NOT MODIFY ANY OF THE CODE ABOVE THIS LINE */

//No Use of free()--Memory Leak
void f1(void) { 
   float a = 90.24;
   float *c = malloc(sizeof(float));
   assert(c != NULL);
   *c = 24.9;
   swap(&a, c);
   printf("%5.2f %5.2f\n", a, *c);
}

//Unchecked malloc of *cp--assert(cp!=NULL) should be used
void f2(void) {
   float ar[3] = {1.1, 2.2, 3.3};
   float *cp = malloc(3 * sizeof(float));
   //error 
   copy(ar, cp, 3);
   print(cp, 3);
}

//double free of cp--In the function print already freed cp
void f3(void) {
   float ar[3] = {-1.0, 0.0, 1.0};
   float *cp = malloc(3 * sizeof(float));
   assert(cp != NULL);
   copy(ar, cp, 3);
   print(cp, 3);
   free(cp);//error
}

//buffer overflow in cp[2]--There is no cp[2] since there is only two elements cp[0] and cp[1]
void f4(void) {
   float ar[2] = {3.14159, 2.71828};
   float *cp = malloc(2 * sizeof(float));
   assert(cp != NULL);
   copy(ar, cp, 2);
   printf("%5.2f %5.2f\n", cp[1], cp[2]);//error
   free(cp);
}

//uninitialised read of cp[2] 
void f5(void) {
   float ar[3] = {1.2, 0.3, -1.4};
   float *cp = malloc(3 * sizeof(float));
   assert(cp != NULL);
   copy(ar, cp, 2);
   print(cp, 3);//error
}

//invalid free--ar isn't been allocated there's no need of free ar
void f6(void) {
   float ar[2] = {1.41421, 1.73205};
   float *cp = malloc(2 * sizeof(float));
   assert(cp != NULL);
   copy(ar, cp, 2);
   print(cp, 2);
   free(ar);//error
}

//no memory allocated--There's no allocated memory for c
void f7(void) {
   float a = 1.1*1.2;
   float *c;
   assert(c != NULL);
   *c = 1.3*1.4;
   swap(&a, c);
   printf("%5.2f %5.2f\n", a, *c);
   free(c);
}

//dangling pointer--*cp already been freed 
void f8(void) {
   float *cp = malloc(sizeof(float));
   assert(cp != NULL);
   *cp = 1.66667;
   float a[1] = {2.33333};
   swap(&a[0], cp);
   free(cp);
   printf("%5.2f %5.2f\n", a[0], *cp);
}


int main(void) {
   printf("f1: ");
   f1();
   printf("f2: ");
   f2();
   printf("f3: ");
   f3();
   printf("f4: ");
   f4();
   printf("f5: ");
   f5();
   printf("f6: ");
   f6();
   printf("f7: ");
   f7();
   printf("f8: ");
   f8();

   return 0;
}
```