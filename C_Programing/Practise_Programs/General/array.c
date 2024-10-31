#include<stdio.h>
//this is a program about array

int main(){
    int array[10], i, sum = 0;

    printf("Enter 10 elements for the array: ");
    for( i = 0;i<10; i++){
        scanf("%d", &array[i]);
    }

    for( i =0; i<10; i++)
    sum += array[i];

    printf("The sum of all the 10 numbers is %d", sum);



    return 0;
}