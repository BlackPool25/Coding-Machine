#include<stdio.h>
#include "grades.c"

int main(){
    int marks;
    printf("Enter the marks of the student (0-100): ");
    scanf("%d", &marks);
    
    char grade = grades(marks);
    if(grade == 'X'){
        printf("Invalid marks entered. Please enter a value between 0 and 100.");
        return 0;
    }
    else{
    printf("Grade: %c", grade);
    }
}

