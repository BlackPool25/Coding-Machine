#include<stdio.h>

int main(){
    int num;
    int is_prime=1;

    printf("Enter the number: ");
    scanf("%d", &num);

    if(num<2){
        printf("Number is not prime.\n");
        return 0;
    }

    for(int i=2;i<=num/2;i++){
        if(num%i==0){
            is_prime = 0;
        }
    }

    if(is_prime){
        printf("It is a prime number.\n");
    }
    
    else{
        printf("It is not a prime number.\n");
    }

    return 0;
}