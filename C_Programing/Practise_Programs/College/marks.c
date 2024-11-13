#include<stdio.h>

int main(){
    int marks;
    printf("Enter the marks: ");
    scanf("%d", &marks);
    if(marks<0 || marks>100){
        printf("Invalid marks");
    }
    else if(marks>=90){
        printf("Grade A");
    }
    else if(marks>=80){
        printf("Grade B");
    }
    else if(marks>=70){
        printf("Grade C");
    }
    else if(marks>=60){
        printf("Grade D");
    }
    else if(marks>=50){
        printf("Grade E");
    }
    else if(marks>=0){
        printf("Fail");
    }
    
    printf("\n");
    return 0;
}