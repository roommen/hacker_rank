#include <iostream>
using namespace std;

int max_of_four(int a, int b, int c, int d) {
    int big = -9999;
    if (a > big)
        big = a;
    if (b > big)
        big = b;
    if (c > big)
        big = c;
    if (d > big)
        big = d;
    return big;
}

int main(int argc, char **argv) {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << max_of_four(a, b, c, d);
    return 0;
}
