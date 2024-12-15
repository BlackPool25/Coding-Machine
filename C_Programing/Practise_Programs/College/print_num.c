#include<stdio.h>

void printnum();

int main(){
    printnum();
    return 0;
}

void printnum(){
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    for(int i=1;i<=n;i++){
        printf("%d\n", i);
    }
}