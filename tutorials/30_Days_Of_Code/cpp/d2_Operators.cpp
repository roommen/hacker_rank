#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char **argv)
{
    double mealCost, totalCost, tipPercent, taxPercent;

    cin >> mealCost >> tipPercent >> taxPercent;
    cin.ignore();

    totalCost = mealCost + ((tipPercent/100) * mealCost) + ((taxPercent/100) * mealCost);
    cout << "The total meal cost is " << round(totalCost) << " dollars." << endl;

    return 0;
}