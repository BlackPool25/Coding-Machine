//SUM OF TWO NUMBERS USING FUNCTIONS
#include <stdio.h>
#include <math.h>

int sum(int,int);

int main(){
    int a,b;
    
    printf("ENTER NUMBER a =");
    scanf("%d" ,&a);
    
    printf("ENTER NUMBER b =");
    scanf("%d" ,&b);

    int s = sum(a,b);

    printf("SUM IS : %d" ,s);

    return 0;
}


int sum(int a,int b){    
    return a+b;
}


