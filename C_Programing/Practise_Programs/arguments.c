#include<stdio.h>


void birthday(char x[], int y){
    printf("\nHappy Birthday Dear %s!", x);
    printf("\nYou are %d years old.", y);
}

int main()
{
    char name[] = "Shreyas";
    int age = 17;

    birthday(name,age);

    return 0;
}