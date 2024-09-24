#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "rotation_question.c"

int is_rotationally_same(char char_t[]);


int main(){
    int user_inp;
    char char_user_inp[20];

    printf("Enter the number to be checked: ");
    if(scanf("%d", &user_inp) != 1){
        printf("Invalid input.");
        return 0;
    }
    sprintf(char_user_inp, "%d", user_inp);

    if(is_rotationally_same(char_user_inp)){
        printf("Yes, the number reads the same upside-down.");
    }
    else{
       printf("No, the number does not read the same upside-down."); 
    }
}

