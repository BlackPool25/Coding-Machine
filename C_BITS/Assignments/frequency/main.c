#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "frequency.c"

int main(){
    int user_input;
    int find_num;
    printf("Enter the number: ");
    if(scanf("%d", &user_input) != 1){
        printf("Invalid input.");
        return 0;
    }
    
    printf("What is the number to find frequency of (0-9): ");
    if(scanf("%d", &find_num) != 1){
        printf("Invalid input.");
        return 0;
    }
    
    int result = frequency(user_input, find_num);
    printf("The frequency of the number repeating is: %d", result);

}
