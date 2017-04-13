#include <stdio.h>
#include <string.h>

int main()
{
	int T;
	scanf("%d", &T);

	while (T > 0)
	{
		char s[10000];
		scanf("%s", s);
		int len_s = strlen(s);
		int i = 0;
		for(i=0; i<len_s; i+=2)
		{
			printf("%c", s[i]);
		}
		printf(" ");
		for(i=1; i<len_s; i+=2)
		{
			printf("%c", s[i]);
		}
		puts("");
		T -= 1;
	}

	return 0;
}

