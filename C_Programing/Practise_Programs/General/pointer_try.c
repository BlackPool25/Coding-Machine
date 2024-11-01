#include<stdio.h>

int sum(int *, int *);

int sum(int * a, int * b){
    return *a+*b;
}


int main(){
    int a,b;
    printf("Enter two nums: ");
    scanf("%d %d", &a, &b);

    printf("The sum is %d", sum(&a, &b));
    return 0;
}