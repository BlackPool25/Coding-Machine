#include<stdio.h>

int getmax(int x, int y){
    return (x>y) ? x : y ;
}

int main(){
    int max = getmax(3,4);
    printf("%d", max);
    return 0;
}