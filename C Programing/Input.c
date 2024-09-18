#include<stdio.h>
#include<string.h>

int main(){
    char name[20]; //bytes
    int age;


    printf("What's your name: ");
    // scanf("%s", &name);
    fgets(name, 25, stdin);
    name[strlen(name)-1] = '\0';

    printf("How old are you: ");
    scanf("%d", &age);

    printf("Your name is %s\n", name);
    printf("You are %d years old", age);


    return 0;

}