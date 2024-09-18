#include<stdio.h>

int main(){

    int marks;

    printf("\nEnter your marks: ");
    scanf("%d", &marks);

    if (marks>90)
    printf("You are graded 'A'.");

    else if (marks >80 && marks <=90)
    printf("You are graded 'B'.");

    else if(marks > 70 && marks <=80)
    printf("You are graded 'C'.");

    else
    printf("You failed!");



    return 0;
}