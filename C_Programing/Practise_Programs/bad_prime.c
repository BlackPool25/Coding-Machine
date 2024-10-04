#include<stdio.h>

int main(){
    long long int num;
    printf("Enter a number: ");
    scanf("%lld", &num);
    if(num==2){
        printf("Prime num");
        return 0;
    }
    else{
        for(int i = 2; i < num; i++){
            if(num % i == 0){
                printf("Not a prime num");
                return 0;
            }
        }
        printf("Prime num");
        return 0;
    }
}