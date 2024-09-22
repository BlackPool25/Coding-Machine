#include<stdio.h>

char report(int marks);

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


char report(int marks){
    if(marks>=90){
        return 'A';
    }
    else if(marks>=80){
        return 'B';
    }
    else if(marks>=70){
        return 'C';
    }
    else if(marks>=60){
        return 'D';
    }
    else if(marks>=50){
        return 'E';
    }
    else if(marks>=0){
        return 'F';
    }
}