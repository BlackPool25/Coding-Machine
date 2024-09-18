#include<stdio.h>

int main(){

    char grade;
    printf("Enter your grade: ");
    scanf("%c", &grade);

    switch(grade){
        case 'A':
            printf("Perfect!\n");
            break;

        case 'B':
            printf("You did good!\n");
            break;

        case 'C':
            printf("You did okay.\n");
            break;

        case 'D':
            printf("At least it's not an F!\n");
            break;
        
        case 'F':
            printf("You FAILED!\n");
            break;

        default:
            printf("Invalid Grade.");
        
            }


    return 0;

}