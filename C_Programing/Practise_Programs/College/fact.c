#include<stdio.h>

int main(){
    int num,fact=1;
    printf("Enter the num: ");
    scanf("%d", &num);

    int i=1;
    while(i++<=num){
        fact *= i;
    }
    printf("The fact is %d", fact);
    return 0;
}