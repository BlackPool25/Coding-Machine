#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int frequency(int num, int target);

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

int frequency(int num, int target){
    int freq = 0;
    char char_num[30];
    char char_target = target + '0';

    sprintf(char_num, "%d", num);

    int size = strlen(char_num);
    for(int i=0;i<size;i++){
        if(char_num[i] == char_target){
            freq++;
        }
    }
    return freq;
}