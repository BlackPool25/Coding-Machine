#include<stdio.h>
#include<string.h>

struct Player{
    char name[20];
    int score;
};

int main(){
    struct Player player1,player2;
    printf("Enter the name of the player: ");
    scanf("%[^\n]%*c", player1.name);
    printf("Enter the score of %s: ", player1.name);
    scanf("%d", &player1.score);
    getchar();

    printf("Enter the name of the player: ");
    scanf("%[^\n]%*c", player2.name);
    printf("Enter the score of %s: ", player2.name);
    scanf("%d", &player2.score);

    printf("%s : %d\n", player1.name, player1.score);
    printf("%s : %d\n", player2.name, player2.score);

    return 0;
}