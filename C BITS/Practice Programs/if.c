#include<stdio.h>

int main(){
    int x;

    // if (0){
    //     printf("Hello");
    // }

    printf("\nEnter a number: ");
    scanf("%d", x);

    if (x>0){
        printf("\nIt is positive.");
    }

    else{
        printf("\nIt is not positive.");
    }

    return 0;
}