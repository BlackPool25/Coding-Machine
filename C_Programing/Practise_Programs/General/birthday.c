#include<stdio.h>

void birthday(){
    printf("\nHappy birthday to you!");
    printf("\nHappy birthday to you!");
    printf("\nHappy birthday dear.....YOU!");
    printf("\nHappy birthday to you!\n");
}

int main(){
    int times;
    printf("How many times do you want it to sing happy birthday: ");
    scanf("%d", &times);
    for(int i=0;i<times;i++){
    birthday();
    }
    return 0;
}