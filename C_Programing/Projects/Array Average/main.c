#include<stdio.h>
#define SIZE 9
#include "avg.c"

int main(){
    int intarray[SIZE], Average;
    for(int i =0;i<SIZE; i++){
        intarray[i]=i;
        printf("%d\t", intarray[i]);
            }
    Average = avg(SIZE,intarray);
    printf("\nThe Average is %d", Average);
    printf("\nAfter calling the function the new array is: \n");
    for(int i=0;i<SIZE; i++)
    printf("%d\t", intarray[i]);
    return 0;
}