#include<string.h>
#include<stdio.h>

int main(){
    char rotated_t[20] = "69";
    char i[10] = "1";
    printf("%s", strcat(rotated_t, (char[]){i[0], '\0'}));
}