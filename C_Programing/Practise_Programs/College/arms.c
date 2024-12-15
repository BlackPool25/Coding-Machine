#include<stdio.h>
#include<math.h>


void arms();

int main(){
    arms();
    return 0;
}

void arms(){
    int num,org,sum=0,digit=0;
    printf("Enter the num: ");
    scanf("%d", &num);

    org = num;
    while(num!=0){
        digit++;
        num/=10;
    }
    num = org;
    while(num!=0){
        sum+=pow(num%10,digit);
        num/=10;
    }

    if(sum==org){
        printf("It is an armstrong num.\n");
    }
    else{
        printf("It is not an armstrong num.\n");
    }

}