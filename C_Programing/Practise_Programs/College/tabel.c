#include<stdio.h>
#include<stdlib.h>

int main(){
    system("clear");
    int num;
    printf("Enter the table number: ");
    scanf("%d", &num);

    for(int i=1;i<=10;i++){
        printf("%d x %d = %d\n", num, i, num*i);
    }
    return 0;
}