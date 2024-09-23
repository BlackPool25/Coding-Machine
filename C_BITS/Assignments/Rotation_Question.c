#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int is_rotationally_same(char char_t[]);


int main(){
    char user_inp[20];
    printf("Enter the number to be checked: ");
    scanf("%s", &user_inp);
    if(is_rotationally_same(user_inp)){
        printf("Yes, the number reads the same upside-down.");
    }
    else{
       printf("No, the number does not read the same upside-down."); 
    }
}


int is_rotationally_same(char char_t[]){
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
            return 0;
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
        return 1;
    }
    else{
        return 0;
    }
}