#include <iostream>
using namespace std;

int main(int argc, char **argv) {
    int num;
    cin >> num;

    if (num == 1)
        cout << "one";
    if (num == 2)
        cout << "two";
    if (num == 3)
        cout << "three";
    if (num == 4)
        cout << "four";
    if (num == 5)
        cout << "five";
    if (num == 6)
        cout << "six";
    if (num == 7)
        cout << "seven";
    if (num == 8)
        cout << "eight";
    if (num == 9)
        cout << "nine";
    if (num > 9)
        cout << "Greater than 9";

    return 0;
}