#include<stdio.h>

void (*push)(char[]) = printf;

int main(){
    // char *p = "Home";
    // char **p1 = &p;

    push("Hello");
    return 0;
}


