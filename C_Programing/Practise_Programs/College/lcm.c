#include<stdio.h>
#include<stdlib.h>

int main(){
    system("clear");
    int a, b, lcm;
    printf("Enter the numbers: ");
    scanf("%d %d", &a, &b);

    // Start with the larger of a and b
    lcm = (a > b) ? a : b;

    // Loop until we find a multiple of both a and b
    while (1) {

        if (lcm % a == 0 && lcm % b == 0) {
            printf("The LCM is %d\n", lcm);
            break;
        }

        lcm += (a > b) ? a : b;  // Increment by the larger number
    }

    return 0;
}