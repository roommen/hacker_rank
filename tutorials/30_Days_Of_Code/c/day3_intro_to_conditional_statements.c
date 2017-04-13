#include <stdio.h>

int main()
{
	unsigned n;
	scanf("%ud", &n);

	if (n % 2 != 0)
	{
		printf("Weird\n");
	}
	else
	{
		if (n >= 2 && n <= 5) {
			printf("Not Weird\n");
		}
		else if (n >= 6 && n <= 20) {
			printf("Weird\n");
		}
		else if (n > 20) {
			printf("Not Weird\n");
		}
	}

	return 0;
}

