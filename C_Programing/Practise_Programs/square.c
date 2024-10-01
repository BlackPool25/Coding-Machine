#include<stdio.h>

int main(){
    float side, area;
    printf("What is the length of the side: ");
    scanf("%f", &side);
    area = side*side;
    printf("The area of the square is: %f \n", area);
    return 0;
}