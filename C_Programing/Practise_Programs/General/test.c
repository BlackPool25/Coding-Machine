#include <stdio.h>

int main() {
    float X = 0.2;
    double A = X / 0.1;
    printf("A = %1f\n", A);

    int p = 3, q = 100;
    double B;
    B = q / (double)p;
    printf("B = %1f\n", B);

    return 0;
}