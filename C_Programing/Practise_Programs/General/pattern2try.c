#include<stdio.h>
int main(){
    int n,i,j,num,gap;
    printf("Enter the number of rows: ");
    scanf("%d", &n);
    gap = n-1;

    for(i=1;i<=n;i++){
        num = i;

        for(j = 1;j <= gap;j++){
            printf(" ");
        }
        gap--;

        for(j = 1;j<=i;j++){
            printf("%d", num);
            num++;
        }

        num--;
        num--;
        for(j=1;j<i;j++){
            printf("%d", num);
            num--;
        }
        printf("\n");
    }


    return 0;
}