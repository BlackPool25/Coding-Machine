#include<stdio.h>

int getnum();

int main(){
    int num = getnum();
    printf("The number you have entered is %d.\n", num);
}

int getnum(){
    int n;
    printf("Enter an integer: ");
    scanf("%d", &n);
    return n;
}