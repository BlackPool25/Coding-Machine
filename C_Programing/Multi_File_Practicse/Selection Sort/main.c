#include<stdio.h>
#include "selectionsort.c"
#define SIZE 8

int main(){
    int array[SIZE];
    printf("\nEnter the 8 elements: ");
    for(int i = 0; i<SIZE; i++){
        scanf("%d", &array[i]);
    }
    selectionsort(array,SIZE);
    printf("\nThe sorted array is: ");
    for(int i=0;i<SIZE;i++)
    printf("\t%d", array[i]);
    return 0;
}