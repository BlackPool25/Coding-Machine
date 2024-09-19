#include <stdio.h>

int main() {
    int i, j, n;

    // Enter the value of n
    printf("Enter the value of N: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        // Print leading spaces
        for (j = i; j < n; j++) {
            printf(" ");
        }
        
        // Print increasing numbers
        for (j = 1; j <= i; j++) {
            printf("%d", j);
        }
        
        // Print decreasing numbers
        for (j = i-1; j >= 1; j--) {
            printf("%d", j);
        }
        
        // Move to the next line
        printf("\n");
    }

    return 0;
}
