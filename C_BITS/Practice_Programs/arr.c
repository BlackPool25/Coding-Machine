#include <stdio.h>

int main() {
    int arr[6][7];

    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 7; j++) {
            arr[i][j] = 2 * (i + j);
        }
    }

    if (arr[3][2] == arr[2][3]) {
        printf("True");
    } else {
        printf("False");
    }

    return 0;
}