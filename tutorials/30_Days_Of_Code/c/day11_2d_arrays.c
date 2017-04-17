#include <stdio.h>
#include <stdlib.h>

int main()
{
	int A[6][6];
	int i, j;
	for (i = 0; i < 6; i++)
	{
		for(j = 0; j < 6; j++)
		{
			scanf("%d", &A[i][j]);
		}
	}

	int sum[20] = {0};
	int ctr = 0, step1 = 0, sum_ = 0;
	for (ctr = 0; ctr < 4; ctr++)
	{
		for(step1 = 0; step1 < 4; step1++)
		{
			int row1_sum = A[ctr][step1] + A[ctr][step1+1] + A[ctr][step1+2];
			int row2_sum = A[ctr+1][step1+1];
			int row3_sum = A[ctr+2][step1] + A[ctr+2][step1+1] + A[ctr+2][step1+2];
			sum[sum_] = row1_sum + row2_sum + row3_sum;
			sum_ ++;
		}
	}

	int largest = -35000;
	for (i=0; i<16;i++)
	{
		// printf("%d\n", sum[i]);
		if (sum[i] > largest)
		{
			largest = sum[i];
		}
		i++;
	}

	printf("%d\n", largest);
	return 0;
}

