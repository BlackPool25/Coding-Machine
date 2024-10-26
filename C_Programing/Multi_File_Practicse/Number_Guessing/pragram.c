#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int get_random(){
    srand(time(0));
    int MIN = 1, MAX = 100;
    return (rand() % MAX) + MIN;
}


int main(){
    int answer = get_random();
    int guess;
    do{
        printf("Guess a number: ");
        scanf("%d", &guess);
        if(guess>answer){
            printf("Too high!\n");
        }
        else if(guess<answer){
            printf("Too low!\n");
        }
    }while(guess != answer);

    printf("You win! The number was %d", answer);
    return 0;
}