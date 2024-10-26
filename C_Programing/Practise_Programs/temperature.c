#include<stdio.h>
int main(){
    float celsius, faranheit;
    printf("\nEnter the temperature in celsius scale: ");
    scanf("%f", &celsius);

    faranheit = celsius * 9 / 5.0 + 32 ;

    printf("\nThe temperature in faranheit scale is %.2f", faranheit);

    return 0;
} 