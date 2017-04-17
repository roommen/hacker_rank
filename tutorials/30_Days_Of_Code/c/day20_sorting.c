#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n;
	scanf("%d", &n);
	
	int *A = (int *)malloc(n * sizeof(int));
	int i, j, k, numSwaps = 0;
	
	for(i=0;i<n;i++)
	{
		scanf("%d", &A[i]);
	}
	
	for (i=0; i<n; i++)
	{
		k = i+1;
		for (j=0; j<n-k; j++)
		{
			if (A[j] > A[j+1])
			{
				int temp;
				temp = A[j+1];
				A[j+1] = A[j];
				A[j] = temp;
				numSwaps++;
			}
		}
	}

	printf("Array is sorted in %d swaps.\n", numSwaps);
	printf("First Element: %d\n", A[0]);
	printf("Last Element: %d\n", A[n-1]);
	return 0;
}

