#include<stdio.h>
#include<stdbool.h>
#include "prime.c"

int main(){
    int choice;
    bool continue_program = true;
    while (continue_program){

    
    int num;
    printf("\nEnter a number to check: ");
    scanf("%u", &num);
    
    prime(num);
    printf("\nDo you want to try again yes(1), no(2): ");
    scanf("%d", &choice);
    if (choice == 2)
    continue_program = false;
    }
    return 0;
}