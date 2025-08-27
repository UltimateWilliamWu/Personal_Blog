#include <stdio.h>

// 函数声明
void quickSort(int array[], int low, int high);
int partition(int array[], int low, int high);

// 主函数
int main() {
    int data[] = {8, 7, 6, 1, 0, 9, 2};
    int size = sizeof(data) / sizeof(data[0]);

    printf("Unsorted Array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");

    // 调用快速排序
    quickSort(data, 0, size - 1);

    printf("Sorted Array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");

    return 0;
}

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
