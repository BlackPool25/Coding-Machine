#include<Stdio.h>
#define N 10
int main(){


    int index = 1, sum = 0;
    while(index <= N)
    {
        sum+=index;
        index++;
    }

    printf("The sum of %d positive positive integers is %d", N, sum);

    return 0;
}