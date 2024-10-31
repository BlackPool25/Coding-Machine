#include<stdio.h>

int main(){
    int start,end,difference,limit, choice,sum=0;
    printf("Enter the starting number: ");
    scanf("%d", &start);

    printf("Enter the common difference: ");
    scanf("%d", &difference);

    printf("Would you like to enter a number of numbers(1) or a Ending number(2) : ");
    scanf("%d", &choice);

    if (choice == 2){
    printf("Enter the ending number: ");
    scanf("%d", &end);

    while(start<=end){
        sum += start;
        start += difference;
    }
    }
    else if (choice == 1){
        int number = 1;
        printf("Enter the number of numbers: ");
        scanf("%d", &limit);

        while(number<=limit)
        {
            sum+=start;
            start+=difference;
            number++;
        }
    
    }
    else
    {
    printf("Invalid Input.");
    return 0;
    }

    printf("The sum is %d", sum);
    return 0;
}