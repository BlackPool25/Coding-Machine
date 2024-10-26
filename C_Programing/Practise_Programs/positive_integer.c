#include<stdio.h>

int main(){

    int num;
    printf("Enter a postive integer: ");
    scanf("%d", &num);
    while(num<=0)
    {
        printf("\nPlease enter a postive integer: ");
        scanf("%d", &num);

        if(num<0)
        printf("You have entered a non-positive number.\n");
    }
    printf("The square of %d is : %d", num, num*num);



    return 0;
}