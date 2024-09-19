#include <stdio.h>

int main() {
    int n, i, sum;
    
    // Input n
    printf("Enter a number n: ");
    scanf("%d", &n);
    
    // Initialize variables
    i = 1;
    sum = 0;
    
    // While loop to calculate sum
    while (i <= n) {
        sum = sum + i;
        i = i + 1;
    }
    
    // Output sum
    printf("The sum is: %d\n", sum);
    
    return 0;
}
