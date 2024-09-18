#include <stdio.h>
int main()
{

    int end; // 1. Try smaller number
    printf("Enter a ending number: ");
    scanf("%d", &end);
    int start = 1;
    unsigned long long i = start, j = 0; // 2. Should we use just int here if 'end' is too large ? Change datatype as mentioned in the ques

    while (i <= end)
    {

        j = i;

        // loop until the current number becomes 1
        while (j != 1)
        {
            if (j % 2 == 0)
            {
                j = j / 2;
            }

            else
            {
                j = (j * 3) + 1;
            }
        }

        // %d id for int, explore %llu
        printf("%llu Passes. \n", i);
        i++;
    }

    return 0;
}
