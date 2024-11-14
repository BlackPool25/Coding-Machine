#include<stdio.h>

void printPat(int rows){
    int i,j;
    for(i = 1;i<=rows;i++){
        for(j=1;j<=rows-i;j++){
            printf(" ");
        }

        for(j=1;j<=i;j++){
            printf("%d", j);
        }

        for(j=i-1;j>=1;j--){
            printf("%d", j);
        }


        printf("\n");
    }

    for(i = rows-1;i>=1;i--){
        for(j=1;j<=rows-i;j++){
            printf(" ");
        }

        for(j=1;j<=i;j++){
            printf("%d", j);
        }

        for(j=i-1;j>=1;j--){
            printf("%d", j);
        }

        printf("\n");
    }
}

int main(){
    int rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    printPat(rows);
    return 0;
}