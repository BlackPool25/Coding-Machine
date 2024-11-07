#include<stdio.h>

int main(){
    int num;
    printf("Enter the num: ");
    scanf("%d", &num);

    int rem = num%5;

    if(rem == 0){
        printf("Divisible.\n");
    }
    else{
        printf("The remainder is %d.\n", rem);
    }
    return 0;
}