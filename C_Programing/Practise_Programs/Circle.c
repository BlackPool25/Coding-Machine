#include<Stdio.h>
#include<math.h>

int main(){

    const double pi = 3.14159;
    double radius,circum, area;
    int choice;

    printf("Enter the radius of the circle: ");
    scanf("%lf", &radius);


    area = pi * pow(radius,2);
    circum = 2 * pi * radius;

    printf("Do you need the circumference(1) or the Area(2): ");
    scanf("%d", &choice);
    if (choice == 1)
    printf("The circumference of the circle is: %lf units", circum);
    else 
    printf("The Area of the circle is %lf square units", area);



    return 0;
}