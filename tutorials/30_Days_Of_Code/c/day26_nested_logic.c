#include <stdio.h>
#include <stdlib.h>

int main()
{
	int ad = 0, am = 0, ay = 0;
	int ed = 0, em = 0, ey = 0;
	int fine = 0;

	scanf("%d%d%d", &ad, &am, &ay);
	scanf("%d%d%d", &ed, &em, &ey);

	if (am == em && ay == ey && ad <= ed)
		fine = 0;

	if (am == em && ay == ey && ad > ed)
		fine = 15 * (ad-ed);

	if (am > em && ay == ey)
		fine = 500 * (am-em);

	if (ay > ey)
		fine = 10000;

	printf("%d", fine);
	return 0;
}

