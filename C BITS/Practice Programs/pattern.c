#include<stdio.h>

int main(){
    int number,rows,columns;
    printf("How many number of rows do you need: ");
    scanf("%d", &number);

    for(rows=1;rows<=number;rows++){

        for(columns=1;columns<=rows;columns++){
            printf("*");
        }
    printf("\n");
    }

    return 0;
}