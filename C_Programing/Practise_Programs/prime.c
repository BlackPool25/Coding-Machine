#include<stdio.h>

int main(){
    int num;
    printf("Enter a num: ");
    scanf("%d", &num);

    for(int i=2;i<=num/2;i++){
        if(num % i == 0){
            printf("It is not a prime number.\n");
            return 0;
        }
    }
    printf("It is a prime number.\n");
    return 0;
}