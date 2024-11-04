#include<stdio.h>

int main(){
    int x=1,y=0;
    int i,j;
    for(i=0;i<5;i++){
        for(j=0;j<5;j++){
            if(i%2==0)
            printf("%d", x);
            else
            printf("%d", y);
        }
        printf("\n");
    }
    return 0;
}