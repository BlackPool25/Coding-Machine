#include<stdio.h>

int main(){
    // char a = 'X';
    // short b = 'Y';
    // double c = 52;
    // short name[20];

    // printf("%d bytes\n", sizeof(a));
    // printf("%d bytes\n", sizeof(b));
    // printf("%d bytes\n", sizeof(c));
    // printf("%d bytes\n", sizeof(name));

    // printf("%p\n", &a);
    // printf("%p\n", &b);
    // printf("%p\n", &c);
    // printf("%p\n", &name);

    int age = 17;
    int *pAge = &age;

    printf("The address of age is %p\n", &age);
    printf("The value of pAge is %p\n\n", pAge);

    printf("The value of age is %d\n", age);
    printf("The value at pAge is %d\n", *pAge); //dereferencing

    printf("The size of age is %d\n", sizeof(age));
    printf("The size of pAge is %d\n", sizeof(pAge));


    return 0;
}