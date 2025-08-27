/*
1. Building the Graph (build_graph())
    This function constructs an adjacency matrix where each pair of numbers is checked to determine if there is a valid transition.
2. Finding the Longest Paths (find_longest_paths())
    This function applies Dynamic Programming (DP) on a Directed Acyclic Graph (DAG).
3. Printing the Longest Paths (print_paths())
    This function recursively prints all longest paths.
Summing up all parts:
    Building the graph: O(n²)
    Finding the longest paths: O(n²)
    Printing all paths: O(n × p) (worst case: exponential)
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAX_N 100
#define MAX_LEN 11  // Max length of int (10 digits) + 1 for null terminator

int numbers[MAX_N];
int graph[MAX_N][MAX_N];  // Adjacency matrix
int n;
int dp[MAX_N];  // DP table for longest path
int parent[MAX_N][MAX_N]; // Store parent nodes for multiple paths
int parent_count[MAX_N];
int max_length;

// Check if b can follow a in a number trail
int is_valid_transition(int a, int b) {
    char str_a[MAX_LEN], str_b[MAX_LEN];
    sprintf(str_a, "%d", a);
    sprintf(str_b, "%d", b);
    int len_a = strlen(str_a), len_b = strlen(str_b);
    
    if (len_a == len_b) {
        int diff_count = 0;
        for (int i = 0; i < len_a; i++) {
            if (str_a[i] != str_b[i]) {
                diff_count++;
            }
        }
        return diff_count == 1;
    } else if (len_b == len_a + 1) {
        for (int i = 0; i < len_b; i++) {
            char temp[MAX_LEN];
            strncpy(temp, str_b, i);
            strcpy(temp + i, str_b + i + 1);
            if (strcmp(temp, str_a) == 0) {
                return 1;
            }
        }
    }
    return 0;
}

// Build adjacency matrix (DAG)
void build_graph() {
    memset(graph, 0, sizeof(graph));
    memset(parent_count, 0, sizeof(parent_count));
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (is_valid_transition(numbers[i], numbers[j])) {
                graph[i][j] = 1;
            }
        }
    }
}

// Find the longest paths using DP on a DAG
void find_longest_paths() {
    memset(dp, 0, sizeof(dp));
    max_length = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (graph[j][i]) {
                if (dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    parent[i][0] = j;
                    parent_count[i] = 1;
                } else if (dp[j] + 1 == dp[i]) {
                    parent[i][parent_count[i]++] = j;
                }
            }
        }
        if (dp[i] > max_length) {
            max_length = dp[i];
        }
    }
}

// Recursive function to print all longest paths
void print_paths(int index, int path[MAX_N], int path_len) {
    path[path_len] = numbers[index];
    path_len++;
    
    if (parent_count[index] == 0) {
        for (int i = path_len - 1; i >= 0; i--) {
            printf("%d%s", path[i], (i == 0) ? "\n" : " -> ");
        }
        return;
    }
    
    for (int i = 0; i < parent_count[index]; i++) {
        print_paths(parent[index][i], path, path_len);
    }
}

int main() {
    printf("Enter a number: ");
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        printf("Enter a number: ");
        scanf("%d", &numbers[i]);
    }
    
    build_graph();
    find_longest_paths();
    printf("\n");
    
    // Task 1: Print possible successors
    for (int i = 0; i < n; i++) {
        printf("%d: ", numbers[i]);
        for (int j = 0; j < n; j++) {
            if (graph[i][j]) {
                printf("%d ", numbers[j]);
            }
        }
        printf("\n");
    }
    
    // Task 2: Find and print all longest paths
    printf("\nMaximum trail length: %d\n", max_length + 1);
    printf("Longest trail(s):\n");
    
    int path[MAX_N];
    for (int i = 0; i < n; i++) {
        if (dp[i] == max_length) {
            print_paths(i, path, 0);
        }
    }
    
    return 0;
}
