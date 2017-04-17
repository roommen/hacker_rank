#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char s[100] = {'\0'};
	scanf("%s", s);

	int len_ = strlen(s);
	int i = 0;
		
	for(i=0; i<len_/2; i++)
	{
		int j = i+1;
		if (s[i] != s[len_ - j])
		{
			printf("The word, %s, is not a palindrome.", s);
			return 0;
		}
	}
	printf("The word, %s, is a palindrome.", s);
	return 0;
}

