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
    while (i >= 0 && array[i] >= array[i + 1]) {
        i--;
    }

    // If no such character is found, it means we are at the last permutation
    if (i < 0) {
        return 0;
    }

    // Find the smallest character on the right of i and larger than array[i]
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
    char array[] = {'c', 'o', 'm', 'p'};
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
