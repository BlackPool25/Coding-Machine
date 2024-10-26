#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
    srand(time(0));
    
    for(int i =0 ;i<100;i++){
    int random_num = (rand() %10)+1;
    printf("The random number is : %d\n", random_num);
    }
    return 0;
}