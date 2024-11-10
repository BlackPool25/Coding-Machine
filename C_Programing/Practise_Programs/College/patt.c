#include <stdio.h>

int main()
{
    int size;
    printf("Enter size: ");
    scanf("%d", &size);

    // Upper part of the pattern
    for(int rows = 1; rows <= size; rows++) {
        for(int spaceCount = rows; spaceCount < size; spaceCount++) {
            printf(" ");
        }
        for(int starCount = 0; starCount < 2 * rows - 1; starCount++) {
            printf("*");
        }
        printf("\n");
    }

    // Lower part of the pattern
    for(int rows = 1; rows <= size - 1; rows++) {
        for(int spaceCount = 0; spaceCount < rows; spaceCount++) {
            printf(" ");
        }
        for(int starCount = 0; starCount < 2 * (size - rows) - 1; starCount++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}