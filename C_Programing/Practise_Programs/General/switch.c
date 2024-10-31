#include<stdio.h>
#include<ctype.h>

int main(){
    char grade;

    printf("Enter a letter grade: ");
    scanf("%c", &grade);
    grade = toupper(grade);

    switch(grade){
        case 'A':
            printf("Perfect!\n");
            break;
        case 'B':
            printf("You did good!\n");
            break;
        case 'C':
            printf("You did okay!\n");
            break;
        case 'D':
            printf("At least it's not an F\n");
            break;
        case 'F':
            printf("You failed!\n");
            break;
        default:
            printf("Enter a valid grade.\n");
    }
    return 0;
}