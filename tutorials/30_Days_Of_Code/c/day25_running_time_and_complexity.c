#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int T;
	scanf("%d", &T);

	int ctr=0, n=0, i=0;
	while (ctr < T)
	{
		int non_prime = 0;
		scanf("%d", &n);

		if (n==1)
		{
			printf("Not prime\n");
			non_prime = 1;
		}

		if (non_prime == 0)
		{
			int sqrt_ = sqrt(n) + 1;
			for (i=2; i<sqrt_; i++)
			{
				if (n % i == 0)
				{
					printf("Not prime\n");
					non_prime = 1;
					break;
				}
			}
		}

		if (non_prime == 0)
			printf("Prime\n");
		ctr++;
	}

	return 0;
}

