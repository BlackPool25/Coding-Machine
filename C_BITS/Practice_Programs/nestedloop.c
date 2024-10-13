#include<stdio.h>

int main(){
    int rows,columns;
    char symbol;
    printf("Enter a symbol: ");
    scanf("%c", &symbol);

    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    printf("Enter the number of columns: ");
    scanf("%d", &columns);

    for(int i=0;i<rows;i++){
        for(int j=0;j<columns;j++){
            printf("%c", symbol);
        }
        printf("\n");
    }
    return 0;
}