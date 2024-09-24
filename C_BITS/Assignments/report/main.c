#include<stdio.h>
#include "report.c"

int main(){
    int marks;
    printf("Enter the marks of the student (0-100): ");
    scanf("%d", &marks);
    if(marks>100 || marks<0){
        printf("Invalid marks entered. Please enter a value between 0 and 100.");
        return 0;
    }
    char grade = report(marks);
    printf("Your grade is %c", grade);
}

