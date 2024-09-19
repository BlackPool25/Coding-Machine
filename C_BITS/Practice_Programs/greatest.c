#include<stdio.h>

int main()
{
    int a,b,c;
    printf("\nEnter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a>b && a>c)
    printf("\nA is the largest.");

    else if (b>a && b>c)
    printf("\nB is the largest.");

    else if (c>a && c>b)
    printf("\nC is the largest.");

    else if ( a==b && b==c )
    printf("\nAll are equal.");

    else 
    printf("END OF PROGRAM.");



    return 0;
}