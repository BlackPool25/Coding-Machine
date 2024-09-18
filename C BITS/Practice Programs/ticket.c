#include<stdio.h>
int main(){
    int age;
    float money;
    printf("\nEnter your age: ");
    scanf("%d", &age);

    if (age<18){
        printf("You are underage!");
        return 0;
    }
    printf("How much money do you have: ");
    scanf("%f", &money);

    printf("You are %d years old and you have $%.2f.", age, money);

    return 0;
}