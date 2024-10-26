#include<stdio.h>
#include<Stdlib.h>

int main(){
    int num,sum = 0,loop_num;
    int iterate = 1;
    printf("\nHow many times do you want to run the loop: ");
    scanf("%d", &loop_num);
    while (iterate <= loop_num){
        printf("Enter a positive number:");
        scanf("%d", &num);

        if (num<0){
        iterate++;
        continue;
        }

        else if (num == 0)
        break;

        sum+=num;
        iterate++;
    }

    printf("\nThe total sum of the positive numbers is %d", sum);

    return 0;
}