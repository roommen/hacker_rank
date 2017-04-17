#include <stdio.h>
#include <stdlib.h>
#include <regex.h>

int main()
{
	int N;
	scanf("%d", &N);
	regex_t regex;

	int ctr = 0;
	while (ctr < N)
	{
		char fname[20] = {'\0'};
		char email[50] = {'\0'};
		scanf("%s %s", fname, email);
		regcomp(&regex, "[a-z]{1,50}@gmail[.]com", REG_EXTENDED);
		int status = regexec(&regex, email, (size_t) 0, NULL, 0);

		if (status == 0)
			printf("%s\n", fname);
		ctr++;
	}

	return 0;
}

