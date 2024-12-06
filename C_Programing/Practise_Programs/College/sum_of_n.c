#include<stdio.h>

int main(){
    int n,sum=0;
    
    printf("Enter the n: ");
    scanf("%d", &n);
    int i;
    for(i=1;i<=n;i++){
        sum += i;
    }
    printf("The sum is %d\n", sum);
    return 0;
}