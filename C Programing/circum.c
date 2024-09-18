#include<stdio.h>

int main(){
    //variables
    float pi, radius, circum;
    pi = 3.14;

    //input
    printf("What is the radius: ");
    scanf("%f", &radius);

    //compute
    circum = 2 * pi * radius;

    //output
    printf("The circumference of the circle is: %f units", circum);
    
}