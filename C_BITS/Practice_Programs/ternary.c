#include<stdio.h>

int main(){
    //ternary operator
    // (condition) ? value if true : value if false
    int num1,num2;
    printf("Enter a number: ");
    scanf("%d", &num1);
    printf("Enter another number: ");
    scanf("%d", &num2);
    num1 > num2 ? printf("Num1 is greater") : printf("Num1 is not greater");
    return 0;
}