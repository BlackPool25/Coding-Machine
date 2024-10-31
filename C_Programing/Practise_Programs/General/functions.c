#include<stdio.h>

void birthday(){
    printf("\nHappy Birthday to you!");
    printf("\nHappy Birthday to you!");
    printf("\nHappy birthday dear....YOU!");
    printf("\nHappy Birthday to you!\n\n");

}

int main(){
    int num;
    printf("How many times do you want to sing 'Happy Birthday'");
    scanf("%d", &num);

    for(int i=0; i<num; i++){
        birthday();
    }
    return 0;
}