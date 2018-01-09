#include <iostream>
#include <cmath>
using namespace std;

void update(int *c,int *d) {
    cout << *c + *d << endl;
    cout << abs(*c - *d) << endl;
}


int main(int argc, char **argv) {
    int a, b;
    int *pa = &a, *pb = &b;
    cin >> a >> b;

    update(pa, pb);

    return 0;
}