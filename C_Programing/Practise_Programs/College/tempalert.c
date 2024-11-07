//temp checking program

#include<stdio.h>

int main(){
    float temp;
    printf("Enter the temp: ");
    scanf("%f", &temp);
    //checking if it is more than 30
    if(temp >30){
        printf("High temp alert.\n");
    }
    //if not do nothing
    return 0;
}