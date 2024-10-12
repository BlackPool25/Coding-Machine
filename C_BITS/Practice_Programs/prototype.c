#include<stdio.h>

//function prototype
void hello(char[],int);


int main(){
    char name[] = "Shreyas";
    int age = 17;
    hello(name, age);
}


void hello(char name[], int age){
    printf("\nHello %s", name);
    printf("\nYou are %d years old.", age);
}