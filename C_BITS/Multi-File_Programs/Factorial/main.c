#include<stdio.h>
#include "fact.c"

int main(){
    int num, factorial;
    printf("\nEnter a number to find a factorial of: ");
    scanf("%d", &num);
    factorial = fact(num);
    printf("\nThe facorial of %d is %d", num, factorial);

    return 0;
}