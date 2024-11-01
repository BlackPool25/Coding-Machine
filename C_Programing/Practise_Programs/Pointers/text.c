#include<stdio.h>

void print_name(char * name){
    printf("%s", name);
}

int main()
{
    char name[] = "Shreyas";
    char * pName = name;

    print_name(pName);
    return 0;
}