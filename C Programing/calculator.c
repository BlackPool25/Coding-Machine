#include<stdio.h>

int main(){

    char operator;
    double num1,num2,result;

    printf("\nEnter the operator:");
    scanf("%c", &operator);

    printf("\nEnter the first number: ");
    scanf("%lf", &num1);

    printf("\nEnter the second number: ");
    scanf("%lf", &num2);

    switch(operator){
        case '+':
        result = num1 + num2;
        printf("\nThe sum of %lf and %lf is %lf",num1 , num2, result);
        break;

        case '-':
        result = num1 - num2;
        printf("\nThe difference of %lf and %lf is %lf",num1 , num2, result);
        break;

        case '*':
        result = num1 * num2;
        printf("\nThe product of %lf and %lf is %lf",num1 , num2, result);
        break;

        case '/':
        result = num1 / num2;
        printf("\nThe quotient of %lf and %lf is %lf",num1 , num2, result);
        break;


        default:
        printf("\nInvalid Operator.");
    }

    return 0;
}