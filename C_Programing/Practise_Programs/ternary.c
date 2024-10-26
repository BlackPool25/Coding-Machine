#include<stdio.h>

int findMax(int x, int y){
    return (x > y) ? x : y;
}


int main(){
    //ternary operator
    // (condition) ? value if true : value if false
    int num1,num2;
    printf("Enter a number: ");
    scanf("%d", &num1);
    printf("Enter another number: ");
    scanf("%d", &num2);
    int max = findMax(num1, num2);
    printf("%d is greater.", max);
    return 0;
}