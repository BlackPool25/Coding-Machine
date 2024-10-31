#include<stdio.h>
#include<math.h>


float find_square_root(float a){
    return sqrt(a);
}


int main(){
    float num,result;
    printf("Enter a number: ");
    scanf("%f", &num);
    result = find_square_root(num);
    printf("Square Root: %f", result);
    return 0;
}