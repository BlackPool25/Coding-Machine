#include<stdio.h>

double square(double x){
    double result = x * x;
    return result;
}


int main(){
    double num, result;
    printf("Enter a number: ");
    scanf("%lf", &num);
    result = square(num);
    printf("The square of the number is %.2lf\n", result);
    return 0;
}