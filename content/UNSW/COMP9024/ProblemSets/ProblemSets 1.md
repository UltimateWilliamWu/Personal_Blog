---
tags:
  - Assignment
---
1. 字母序全排列 alphabetical order
```C
#include <stdio.h>

// Swap two elements
void Swap(char array[], int p, int q) {
    char temp = array[q];
    array[q] = array[p];
    array[p] = temp;
}

// Sort the array in ascending order
void Sort(char array[], int start, int end) {
    for (int i = start; i < end - 1; i++) {
        for (int j = i + 1; j < end; j++) {
            if (array[i] > array[j]) {
                Swap(array, i, j);
            }
        }
    }
}

// Find the next lexicographical permutation
int NextPermutation(char array[], int len) {
    int i = len - 2;

    // Find the first character that is smaller than its successor
    // Find the rightmost character that is smaller than the character next to it
    while (i >= 0 && array[i] >= array[i + 1]) {
        i--;
    }

    // If no such character is found, it means we are at the last permutation
    if (i < 0) {
        return 0;
    }

    // Find the smallest character on the right of i and larger than array[i]
    // Find the smallest character on the right that is larger than this character
    int j = len - 1;
    while (array[j] <= array[i]) {
        j--;
    }

    // Swap characters at i and j
    Swap(array, i, j);

    // Reverse the sequence from i+1 to end
    int start = i + 1, end = len - 1;
    while (start < end) {
        Swap(array, start, end);
        start++;
        end--;
    }

    return 1;
}

int main() {
    char array[] = {'a', 'l', 'g', 'o'};
    int len = sizeof(array) / sizeof(array[0]);

    // Sort the array in lexicographical order
    Sort(array, 0, len);

    // Print the first permutation
    do {
        for (int i = 0; i < len; i++) {
            printf("%c", array[i]);
        }
        printf("\n");
    } while (NextPermutation(array, len));

    return 0;
}

```
2. 队列实现
queue.c
```C
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
```
queue.h
```C
// Character Queue ADO header file
#define MAXITEMS 10

void QueueInit();        // set up empty queue
int  QueueIsEmpty();     // check whether queue is empty
void QueueEnqueue(char); // insert char at end of queue
char QueueDequeue();     // remove char from front of queue
```
- **Challenge Exercise**   
	- A 5-digit number is divisible by a 3-digit number without remainder. Neither number contains the digit 9. 
	- If you increment by 1 each digit of both numbers, then again they can be divided without remainder. 
	- The difference between the results of the two divisions is exactly 100.
```C
#include <stdio.h>

// 检查数字是否包含数字9
int contains_nine(int number) {
    while (number > 0) {
        if (number % 10 == 9) {
            return 1; // 包含数字9
        }
        number /= 10;
    }
    return 0; // 不包含数字9
}

int main(void) {
    // 遍历所有5位数
    for (int num1 = 10000; num1 < 100000; num1++) {
        if (contains_nine(num1)) continue; // 跳过包含9的5位数

        // 遍历所有3位数
        for (int num2 = 100; num2 < 1000; num2++) {
            if (contains_nine(num2)) continue; // 跳过包含9的3位数

            // 检查是否符合初始条件：num1能被num2整除
            if (num1 % num2 == 0) {
                int result1 = num1 / num2;

                // 递增后的数字
                int num1_inc = num1 + 11111;
                int num2_inc = num2 + 111;

                // 检查递增后的条件
                if (!contains_nine(num1_inc) && !contains_nine(num2_inc) &&
                    num1_inc % num2_inc == 0) {
                    // 检查结果的差值是否为100
                    if (num1_inc/num2_inc-num1/num2== 100|| (num1 / num2 - num1_inc / num2_inc == 100)) {
                        // 输出结果
                        printf("5-digit number: %d, 3-digit number: %d\\n", num1, num2);
                        return 0; // 找到答案后退出程序
                    }
                }
            }
        }
    }
    // 如果没有找到符合条件的结果
    printf("No solution found.\n");
    return 0;
}
```
