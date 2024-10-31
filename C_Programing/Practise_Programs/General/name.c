#include<stdio.h>
int main(){
    int num1,num2,result;
    printf("Number 1: ");
    scanf("%d", &num1);
    printf("Number 2: ");
    scanf("%d", &num2);
    result = num1+num2;
    printf("Result:%d+%d = %d\n",num1,num2, result);
    return 0;
}