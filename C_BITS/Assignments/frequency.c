#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int frequency(int num, int target);

int main(){
    int user_input, find_num;
    printf("Enter the number: ");
    scanf("%d", &user_input);
    printf("What is the number to find frequency of (0-9): ");
    scanf("%1d", &find_num);
    int result = frequency(user_input, find_num);
    printf("The frequency of the number repeating is: %d", result);

}

int frequency(int num,int target){
    int freq = 0;
    char char_num[20];
    char char_target = target + '0';

    itoa(num, char_num, 10);

    int size = strlen(char_num);
    for(int i=0;i<size;i++){
        if(char_num[i] == char_target){
            freq++;
        }
    }
    return freq;
}