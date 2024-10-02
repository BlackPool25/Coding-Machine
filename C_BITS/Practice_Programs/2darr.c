#include<stdio.h>
#include<stdlib.h>

void clrscr(){
    system("@cls||clear");
}


int main(){
    clrscr();
    int row = 3;
    int column = 3;
    int size = 20;
    char data[row][column][size];
    for(int i =0; i<row;i++){
        int j = 0;
        printf("Whats the USN: ");
        scanf("%s", data[i][j]);
        j++;
        printf("Enter the name: ");
        scanf("%s", data[i][j]);
        j++;
        printf("Enter the marks: ");
        scanf("%s", data[i][j]);
        clrscr();
    }
    for(int i=0;i<row;i++){
        for(int j=0;j<column;j++){
        printf("%s ", data[i][j]);
        }
        printf("\n");
    }
    return 0;
}