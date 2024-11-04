#include<stdio.h>
#include<stdlib.h>

int main(){
    int *p, *q;
    p = (int*) malloc(10*sizeof(int));
    q = p;
    for(int i = 0;i<10;i++){
        *p = i*i;
        p++;
    }
    for(int i = 0;i<10;i++){
        printf("The element at index %d is %d\n", i , q[i]);
    }
    return 0;
    free(p);
    free(q);
}