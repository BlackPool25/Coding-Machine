#include<stdio.h>

int main(){
    int i,sum=0;
    for(i=1;i<=10000;i++){
        if(i%3==0 && i%4!=0)
        sum+=i;
    }
    printf("The sum is %d", sum);

    return 0;
}