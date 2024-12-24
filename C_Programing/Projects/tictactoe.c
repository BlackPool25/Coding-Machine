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

int checkwin(char box[SIZE][SIZE]){
    for(int i=0;i<SIZE;i++){
        if(box[i][0] == box[i][1] && box[i][1] == box[i][2] && box[i][0] != ' '){
            return 1;
        }
        if(box[0][i] == box[1][i] && box[1][i] == box[2][i] && box[0][i] != ' '){
            return 1;
        }
    }

    if(box[0][0] == box[1][1] && box[1][1] == box[2][2] && box[0][0] != ' '){
        return 1;
    }
    if(box[0][2] == box[1][1] && box[1][1] == box[2][0] && box[0][2] != ' '){
        return 1;
    }
    return 0;
}


int checkdraw(char box[SIZE][SIZE]){
    for(int i=0;i<SIZE;i++){
        for(int j=0;j<SIZE;j++){
            if(box[i][j] == ' '){
                return 0;
            }
        }
    }
    return 1;
}

void playgame(){
    char box[SIZE][SIZE] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    int player = 1, row, col;
    char checker, mark;
    
    while(1){
        display_box(box);
        printf("Player %d's turn (Enter row and column): ", player);
        scanf("%d %d", &row, &col);

        if(row<1 || row>SIZE || col<1 || col>SIZE || box[row-1][col-1] != ' '){
            printf("Invalid Move! Try again.\n");
            continue;
        }

        mark = (player == 1) ? 'X' : 'O';
        box[row-1][col-1] = mark;


        if(checkwin(box)){
            display_box(box);
            printf("Player %d wins!\n", player);
            break;
        }
        else if(checkdraw(box)){
            display_box(box);
            printf("It is a draw!\n");
            break;
        }

        player = (player == 1) ? 2 : 1;
    }
}

int main(){
    printf("Welcome to Tic-Tac-Toe!\n");
    playgame();
    printf("Thank you for playing!\n");
    return 0;
}