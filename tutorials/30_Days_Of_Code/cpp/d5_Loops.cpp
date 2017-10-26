#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int num, i = 1;
    cin >> num;

    while (i <= 10)
    {
        cout << num << " x " << i << " = " << num * i << endl;
        i += 1;
    }
    return 0;
}