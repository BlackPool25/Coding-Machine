#include<stdio.h>

struct Student{
    char name[20];
    int marks1;
    int marks2;
}s1[5];


int main(){
    printf("%d bytes", sizeof(s1));
    return 0;
}