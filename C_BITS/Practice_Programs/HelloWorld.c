#include<stdio.h>
#include<math.h>

int main(){
    const double PI = 3.14159;
    double radius, circumference, area;
    printf("Enter the radius of a circle: ");
    scanf("%lf", &radius);
    circumference = 2 * PI * radius;
    area = PI * pow(radius, 2);
    printf("The circumference of the circle is %.2lf", circumference);
    printf("\nThe area of the circle is %.2lf", area);
    return 0;
}

