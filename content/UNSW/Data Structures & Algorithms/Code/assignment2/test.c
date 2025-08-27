#define SIZE 1000
#include<stdio.h>
#include<stdlib.h>

int *makeArrayOfInts() {
   int *arr=malloc(SIZE*sizeof(int));
   int i;
   for (i=0; i<SIZE; i++) {
      arr[i] = i;
   }
   return arr;
}

int main(void){
    int *result=makeArrayOfInts();
    return 0;
}