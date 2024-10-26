#include <stdio.h>
#include <stdbool.h>

bool is_rotationally_same(int num){
    char char_t[20]; 
    sprintf(char_t, "%d", num);
    int is_allowed[] = {'1', '8', '6', '9', '0'};
    char to_rotate_t[20] = "";
    int length = strlen(char_t);

    for(int i=0;i<strlen(char_t);i++){
        char digit = char_t[i];
        int found = 0;
        for(int j=0;j<5; j++){
            if (digit == is_allowed[j]){
                found = 1;
                break;
            }
        }
        if(!found){
            return false;
        }
    }

    for(int i=0;i<length;i++){
        if(char_t[i] == '6'){
            strcat(to_rotate_t, "9");
        }
        else if(char_t[i] == '9'){
            strcat(to_rotate_t, "6");
        }
        else{
            strcat(to_rotate_t, (char[]){char_t[i], '\0'});
        }
    }

    char rotated_t[20] = "";
    for(int i = length-1; i>-1;i--){
        strcat(rotated_t, (char[]){to_rotate_t[i], '\0'});
    }

    if(atoi(char_t) == atoi(rotated_t)){
        return true;
    }
    
    else{
        return false;
    }
}