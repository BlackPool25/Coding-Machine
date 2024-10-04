#include<stdio.h>
#include<math.h>


int main(){
    long long int num;
    printf("Enter a number: ");
    scanf("%lld", &num);
    if(num < 2){
        printf("Not a prime number\n");
        return 0;
    }
    if(num == 2){
        printf("Prime number\n");
        return 0;
    }
    if((num % 2 == 0) && (num != 2)){
        printf("Not a prime number\n");
        return 0;
    }
    float float_num = (float) num;
    for(int i = 3; i < float_num; i += 2){
        if(num % i == 0){
            printf("Not a prime number\n");
            return 0;
        }
    }
    printf("Prime number\n");
    return 0;
}