#include <stdio.h>
#include <stdlib.h>

int main()
{
	int T;
	scanf("%d", &T);

	int ctr = 0;
	while(ctr < T)
	{
		int N, K, max = 0;
		scanf("%d%d", &N, &K);

		//int *A = (int *)malloc(N * sizeof(int));
		int i;
		for (i=1; i<=N; i++)
		{
			int j;
			for(j=i+1; j<=N; j++)
			{
				int and_ = i & j;
				//printf("and_:%d, i:%d, max:%d\n", and_, i, max);
				if (and_ > max && and_ < K)
					max = and_;
			}
		}
		printf("%d\n", max);
		ctr++;
	}

	return 0;
}


