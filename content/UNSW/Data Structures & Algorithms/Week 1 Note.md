---
tags:
  - LectureNotes
---
[[ProblemSets 1]]
## 1. Sorting Method
### 1.1 Insertion Sort
![[插入排序.png]]
![[插入.gif]]
1. Take the element `a[i]` from the array and assign it to `temp`.
2. Compare `temp` with each element `a[j]` in the sorted portion of the array (all elements before `a[i]`).
3. If `a[j]` is larger than `temp`, shift `a[j]` one position to the right.
4. Continue until the correct position for `temp` is found, and insert `temp` there.

```C
void insertionSort(int arr[],int len){
    int i, j, temp;
	for(i = 1; i < len; i ++)
	{
		temp = arr[i];
		for(j = i - 1; j >= 0; j --)
		{
			if(arr[j] > temp)
			{
				arr[j + 1] = arr[j];	
			}else
			{
				break;
			}
		}
		arr[j + 1] = temp;
	}
}
```
### 1.2 Bubble Sort
1. Swap two elements if first one is bigger than second one
2. loop for n-1 times

![[冒泡.gif]]
```C
void bubbleSort(int arr[],int len){
    for(int i=0;i<len-1;i++){
        for(int j=0;j<len-i-1;j++){
            if(arr[j]>arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
}
```
### 1.3 Selection Sort
1. Find the smallest/biggest number in the unsorted array then swap it with the first unsorted element 
2. Repeat 1 step 
![[选择.gif]]
```C
void selectionSort(int arr[],int len){
	for(int i=0;i<len-1;i++){ //最后一个不用排序
		int minIndex=i;
		for(int j=i+1;j<len;j++){ //已经排序的序列不需要再排序
			if(arr[j]<arr[minIndex]){
				minIndex=j;
			}
		}
		int temp=arr[i];
		arr[i]=arr[minIndex];
		arr[minIndex]=temp;
	}
}
```
### 1.4 Quick Sort
1. **Choose a Pivot(找基准值):** Select an element from the array as the pivot. This could be the first element, the last element, the middle element, or a randomly chosen one.
2. **Partition(分区):** Rearrange the array such that:
    - Elements smaller than the pivot are placed on the left.
    - Elements larger than the pivot are placed on the right.
3. **Recursively Sort(递归):** Apply Quick Sort to the left and right sub-arrays separately.
4. **Combine(合并):** Since the partitioning already places the pivot in its correct position, no further combination is required.

![[快速.gif]]

```C
// 快速排序函数
void quickSort(int array[], int low, int high) {
    if (low < high) {
        // 找到分区点
        int pivotIndex = partition(array, low, high);
        // 递归地对左侧和右侧部分排序
        quickSort(array, low, pivotIndex - 1);
        quickSort(array, pivotIndex + 1, high);
    }
}

// 分区函数
int partition(int array[], int low, int high) {
    int pivot = array[high]; // 选择最后一个元素作为基准
    int i = low - 1;         // 较小元素的索引

    for (int j = low; j < high; j++) {
        if (array[j] < pivot) {
            i++;
            // 交换 array[i] 和 array[j]
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }

    // 交换 array[i + 1] 和 pivot (array[high])
    int temp = array[i + 1];
    array[i + 1] = array[high];
    array[high] = temp;
    return i + 1; // 返回基准的索引
}

```
## 2. Numeral System 
A program that is designed to implement  Conversion Between Different Numeral Systems  
### Using Stack Structure to implement
```C
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
```
