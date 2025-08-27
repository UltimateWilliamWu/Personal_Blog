/* 
Solution 1: Using DFS 
    Building Graph:O(n²)
    DFS Traversal:O(n!) (worst case, exploring all permutations).
    Overall Complexity:O(n²+n!) 

Solution 2: Using DP (Harder but better in time complexity)
    Finding the longest paths: O(n²)
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NUMS 100
#define MAX_LEN 11 // INT_MAX has 10 digits +1 for null terminator

int n;//numbers of input numbers
int numbers[MAX_NUMS];//store input numbers
int adj[MAX_NUMS][MAX_NUMS];//Actually this is just a simple implement of graph 
int maxLength = 0;
int longestPaths[MAX_NUMS][MAX_NUMS];//storing the longest Paths which can be multiple paths
int pathCount = 0;

/**
 * Check if two numbers differ by only one digit as required
 */
int checkValidity(int a, int b) {
    char str_a[MAX_LEN], str_b[MAX_LEN];
    sprintf(str_a, "%d", a); // Converts integer to string
    sprintf(str_b, "%d", b);
    int len_a = strlen(str_a), len_b = strlen(str_b);// Get the length of str_a and str_b
    /**
     * Case 1:
     * Two numbers with the same length but only one different digit
     */
    if (len_a == len_b) { 
        int count = 0;
        for (int i = 0; i < len_a; i++) {
            if (str_a[i] != str_b[i]) {
                count++;
            }
        }
        return count == 1;
    }
    /**
     * Case 2:
     * Two numbers with one digit difference(one more digit)
     */
    else if (len_b == len_a + 1) {
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

// Build adjacency matrix (Can use graph instead)
void build_graph() {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (checkValidity(numbers[i], numbers[j])) {
                adj[i][j] = 1;
            }
        }
    }
}

//Using dfs to find the longest path
/**
 *  index: The current node index being explored
    path[]: Array storing the current path.
    pathLen: Length of the current path.
 */
void dfs(int index, int path[], int pathLen) {
    path[pathLen++] = index;
    if (pathLen > maxLength) { //find better(longer) path
        maxLength = pathLen;
        pathCount = 0;
    }
    if (pathLen == maxLength) { //find multiple answers
        memcpy(longestPaths[pathCount], path, pathLen * sizeof(int));
        pathCount++;
    }
    for (int i = index + 1; i < n; i++) {
        if (adj[index][i]) {
            dfs(i, path, pathLen);
        }
    }
}

/**
 * Solution 2: Using Dynamic Programming (DP)
 */
// Find the longest paths using DP on a DAG
int dp[MAX_NUMS];  // DP table for longest path
int parent[MAX_NUMS][MAX_NUMS]; // Store parent nodes for multiple paths
int parent_count[MAX_NUMS];
void find_longest_paths() {
    memset(dp, 0, sizeof(dp));
    maxLength = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (adj[j][i]) {
                if (dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    parent[i][0] = j;
                    parent_count[i] = 1;
                } else if (dp[j] + 1 == dp[i]) {
                    parent[i][parent_count[i]++] = j;
                }
            }
        }
        if (dp[i] > maxLength) {
            maxLength = dp[i];
        }
    }
}

// Recursive function to print all longest paths
void print_paths(int index, int path[MAX_NUMS], int path_len) {
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
    
    printf("\n");
    for (int i = 0; i < n; i++) {
        printf("%d:", numbers[i]);
        for (int j = i + 1; j < n; j++) {
            if (adj[i][j]) {
                printf(" %d", numbers[j]);
            }
        }
        printf("\n");
    }
    
    int path[MAX_NUMS];
    for (int i = 0; i < n; i++) {
        dfs(i, path, 0);
    }

    printf("\nMaximum trail length: %d\n", maxLength);
    printf("Longest trail(s):\n");
    for (int i = 0; i < pathCount; i++) {
        for (int j = 0; j < maxLength; j++) {
            printf("%d%s", numbers[longestPaths[i][j]],(j == maxLength-1) ? "" : " -> ");
        }
        printf("\n");
    }
    return 0;
}
