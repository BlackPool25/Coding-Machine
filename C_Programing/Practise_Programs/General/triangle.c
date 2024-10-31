#include <stdio.h>

int main() {
    int rows;

    // Prompt user for the number of rows
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
 
    // Loop through each row
    for (int i = 1; i <= rows; i++) {
        // Print '#' i times for the current row
        for (int j = 0; j < i; j++) {
            printf("#");
        }
        // Move to the next line after printing all '#' for the current row
        printf("\n");
    }

    return 0;
}