#include <iostream>
#include <string>
using namespace std;

int main(int argc, char **argv) {
    string s1, s2;
    cin >> s1 >> s2;

    cout << s1.size() << " " << s2.size() << endl;

    cout << s1+s2 << endl;

    char t1 = s1[0];
    char t2 = s2[0];
    s1[0] = t2;
    s2[0] = t1;

    cout << s1 << " " << s2 << endl;

    return 0;
}