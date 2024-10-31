#include<stdio.h>
int d;
void func();

void func(){
    static int g = 0;
    g+=10;
    printf("\nThe value of G is %d", g);
}

int e;

void main(){

int b = 0;
for(int f = 0; f<3 ; f++)
{func();
int c;
}
}