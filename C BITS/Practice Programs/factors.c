#include<stdio.h>

int main(){
    int num_of_factors = 0, number, limit, i, row=0;

    printf("\nEnter the number who's factor you want to find: ");
    scanf("%d", &number);

    printf("\nWhat is the end limit: ");
    scanf("%d", &limit);

    for(i=1;i<=limit;i++){
        if (i%number==0){
            row++;
            num_of_factors++;
            printf("%d ", i);
            
            if (row==10){
                printf("\n");
                row-=10;
            }
        }
        
    
    }
    printf("\nThe total number of factors of the number %d is %d", number, num_of_factors);

    return 0;
}