#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */    
	double mealCost;
	int tipPercent, taxPercent;

	scanf("%lf", &mealCost);
	scanf("%d", &tipPercent);
	double tipAmount = (mealCost * tipPercent)/100;
	scanf("%d", &taxPercent);
	double taxAmount = (mealCost * taxPercent)/100;

	printf("The total meal cost is %.0lf dollars.\n", round(mealCost+tipAmount+taxAmount));

	return 0;
}

