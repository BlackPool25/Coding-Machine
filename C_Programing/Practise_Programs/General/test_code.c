#include <stdio.h>

struct foo {
    float t;
    int u;
};

int main() {
    struct foo f1 = {2, 3.5};
    printf("%f %d", f1.t, f1.u);
}