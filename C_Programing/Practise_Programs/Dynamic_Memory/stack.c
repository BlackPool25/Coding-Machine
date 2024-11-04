#include<stdio.h>

int inf(int a){
    printf("%d\n", a);
}

int main(){
    int a =4;
    while(1)
    {
        inf(a);
        a++;
    }
    return 0;
}