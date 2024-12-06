#include<stdio.h>

//No argument with no return value
void is_even();

int main(){
    is_even();
}

void is_even(){
    int num;
    printf("Enter the num: ");
    scanf("%d", &num);

    if(num%2==0)
    {
        printf("It is even.\n");
    }
    else{
        printf("It is odd.\n");
    }
}
// int main(){
//     greet();
// }

// void greet(){
//     printf("This is a function with no return type.\n");
// }