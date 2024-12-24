#include<stdio.h>
#define SIZE 3

void display_box(char box[SIZE][SIZE]){
    printf("\n");
    for(int i=0;i<SIZE;i++){
        for(int j=0;j<SIZE;j++){
            printf(" %c ", box[i][j]);
            if(j<SIZE-1) printf("|");
        }
        printf("\n");
        if(i<SIZE-1) printf("---+---+---\n");
    }
    printf("\n");
}


void playgame(){
    char box[SIZE][SIZE] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    int player = 1, row, col;
    char checker, mark;
    
    while(1){
        display_box(box);
        printf("Player %d's turn (Enter row and column): ");
        scanf("%d %d", &row, &col);

        if(row<1 || row>SIZE || col<1 || col>SIZE || box[row-1][col-1]!= ' '){
            printf("Invalid Move! Try again.\n");
            continue;
        }

        mark = (player == 1) ? 'X' : 'O';
        box[row-1][col-1] = mark;


        if(checkwin(box)){
            printf("Player %d wins!\n", player);
            return 0;
        }
        else if(checkdraw(box)){
            printf("It is a draw!\n");
            return 0;
        }
        else if(checklose(box)){
            printf("You lose!\n");
            return 0;
        }

        player = (player == 1) ? 2 : 1;
    }
}