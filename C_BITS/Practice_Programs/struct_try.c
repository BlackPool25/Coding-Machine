#include<stdio.h>
#include<string.h>

struct Player{
    char name[20];
    int score;
};


int main(){
struct Player player1;
struct Player player2;

strcpy(player1.name, "Shreyas");
player1.score = 99;

strcpy(player2.name, "Joshi");
player2.score = 100;

printf("%s\n", player1.name);
printf("%d\n", player1.score);

printf("%s\n", player2.name);
printf("%d", player2.score);

return 0;
}