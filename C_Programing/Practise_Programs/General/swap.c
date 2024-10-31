#include<stdio.h>
#include<string.h>

int main(){
    char x[15] = "Water";    //length of str is important
    char y[15] = "Lemonade"; //if one is shorter it may cause unexpected errors
    char temp[15];

    strcpy(temp, x);
    strcpy(x, y);
    strcpy(y, temp);

    printf("x is %s\n", x);
    printf("y is %s\n", y);
    return 0;
}