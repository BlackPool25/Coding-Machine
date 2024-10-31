#include<stdio.h>

int main(){
    int x = 4;
    char name[] = "Shreyas";
    int * px = &x;
    char * pc = name;
    printf("%d", *px);
    printf("Your name is %s", *pc);
    return 0;
}