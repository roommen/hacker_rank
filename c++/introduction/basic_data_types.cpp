#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char **argv) {
    int a;
    long b;
    char c;
    float d;
    double e;

    cin >> a >> b >> c >> d >> e;

    cout << a << endl << b << endl << c << endl << std::setprecision(6) << d << endl
    << std::setprecision(10) << e << endl;

    return 0;
}
