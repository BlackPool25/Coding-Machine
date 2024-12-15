#include <stdio.h>

void printPattern(int rows) {
    int i, j;  // Declare loop variables at the beginning
    
    // Upper part of the pattern
    for (i = 1; i <= rows; i++) {
        // Print leading spaces
        for (j = 1; j <= rows - i; j++) {
            printf("  ");
        }
        
        // Print ascending numbers
        for (j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        
        // Print descending numbers
        for (j = i - 1; j >= 1; j--) {
            printf("%d ", j);
        }
        
        // Newline after each row
        printf("\n");
    }
    
    // Lower part of the pattern
    for (i = rows - 1; i >= 1; i--) {
        // Print leading spaces
        for (j = 1; j <= rows - i; j++) {
            printf("  ");
        }
        
        // Print ascending numbers
        for (j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        
        // Print descending numbers
        for (j = i - 1; j >= 1; j--) {
            printf("%d ", j);
        }
        
        // Newline after each row
        printf("\n");
    }
}

int main() {
    int rows;
    
    // Input the number of rows
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    
    printPattern(rows);
    
    return 0;
}