#include <iostream>
#include <string>
#include <sstream>
using namespace std;


int main(int argc, char **argv) {
    int t;
    cin >> t;
    while (t!=0) {
        int b, s, c;
        cin >> b >> s >> c;
        cout << (b+s) - c << endl;
        --t;
    }

    return 0;
}