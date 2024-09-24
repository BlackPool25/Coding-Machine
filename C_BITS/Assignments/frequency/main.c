#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "frequency.c"

int main(){
    int user_input;
    int find_num;
    printf("Enter a number\n");
    if(scanf("%d", &user_input) != 1){
        printf("Invalid input.");
        return 0;
    }
    
    printf("Enter the digit to be checked\n");
    if(scanf("%d", &find_num) != 1){
        printf("Invalid input.");
        return 0;
    }
    
    int result = frequency(user_input, find_num);
    printf("The frequency of the digit %d in %d is: %d", find_num, user_input, result);

}
