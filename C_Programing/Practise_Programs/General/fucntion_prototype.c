#include<stdio.h>

void hello(char[],int);

int main(){
    char name[] = "Shreyas";
    int age = 17;
    hello(name,age);
    return 0;
}

void hello(char x[],int y){
    printf("\nHello %s!",x);
    printf("\nYou are %d years old.", y);
}