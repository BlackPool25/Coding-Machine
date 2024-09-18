#include<stdio.h>
#define N 4
int main(){

    int index = 1;
    while (index <= N){
        int sum = 0;
        int j = 1, marks;
        while (j<=3){

            printf("\nEnter marks for subject %d : ", j);
            scanf("%d", &marks);
            sum += marks;
            j++;

        }
        float avg = sum/3.0;
        printf("\nAverage marks of student %d is %.2f \n", index, avg);
        
        if (index<N)
        printf("\nNow for the student number %d", index+1);
        index++;
    }

    return 0;
}