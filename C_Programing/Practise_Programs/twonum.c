#include<stdio.h>

int main(){
    int a,b;
    printf("Enter two num: ");
    scanf("%d %d", &a, &b);

    if(a>b){
        printf("%d is greater", a);
    }
    else if(b>a){
        printf("%d is greater", b);
    }
    else
    printf("%d is the same as %d", a, b);
    return 0;
}