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
        break;

        case '-':
        result = num1 - num2;
        break;

        case '*':
        result = num1 * num2;
        break;

        case '/':
        result = num1 / num2;
        break;


        default:
        printf("\nInvalid Operator.");
        return 0;
    }
    printf("%lf %c %lf = %lf\n", num1, operator, num2, result);
    return 0;
}