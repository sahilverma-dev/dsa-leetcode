#include <stdio.h>

void main()
{

    int n = 19;
    // is prime

    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            printf("Not Prime\n");
            break;
        }
        else
        {

            printf("Prime\n");
            break;
        }
    }
}
