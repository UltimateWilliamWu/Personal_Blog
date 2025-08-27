#include <stdio.h>

void insertionSort(int arr[],int len){
    int i, j, temp;
	for(i = 1; i < len; i ++)
	{
		temp = arr[i];
		for(j = i ; j >= 1; j --)
		{
			if(arr[j-1] > temp)
			{
				arr[j] = arr[j-1];	
			}else
			{
				break;
			}
		}
		arr[j] = temp;
	}
}

void selectionSort(int arr[],int len){
    for(int i=0;i<len-1;i++){
        int minIndex=i;
        for(int j=i+1;j<len;j++){
            if(arr[j]<arr[minIndex]){
                minIndex=j;
            }
        }
        int temp=arr[i];
        arr[i]=arr[minIndex];
        arr[minIndex]=temp;
    }
}

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

int main(void){
    int arr[]={3,5,2,4,6,9};
    bubbleSort(arr,6);
    for(int i=0;i<6;i++){
        printf("%d ",arr[i]);
    }
    return 0;
}