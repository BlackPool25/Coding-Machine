#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "rotation_question.c"

int main(){
    int user_inp;

    printf("Enter the number to be checked: ");
    if(scanf("%d", &user_inp) != 1){
        printf("Invalid input.");
        return 0;
    }

    if(is_rotationally_same(user_inp)){
        printf("Yes, the number can be read upside down.");
    }
    else{
       printf("No, the number cannot be read upside down."); 
    }
}

