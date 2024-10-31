#include <stdio.h>
int main() {
    int p = 20;
    int q = 10;
    int r = 15;
    int s = 5;
    int A,B,C,D;
    A = p % s + q * r / s;
    printf("Value of p %% s + q * r / s is : %d\n", A );
    p = 20;
    q = 10;
    r = 15;
    s = 5;
    B = p++ + q * r / s;
    printf("Value of p++ + q * r / s is : %d\n", B );
    p = 20;
    q = 10;
    r = 15;
    s = 5;
    C = p-- + --q - q * r / s;
    printf("Value of p-- + --q - q * r / s is : %d\n", C );
    p = 20;
    q = 10;
    r = 15;
    s = 5;
    D = (++p / (q-3))* s - r;
    printf("Value of (++p / (q-3))* s - r is : %d\n", D );
    return 0;
}
