#include<stdio.h>

int main(){
    int x = 6; //6 = 00000110
    int y = 12; //12 = 00001100

    int z = x ^ y;

    printf("%d", z);
    return 0;
}