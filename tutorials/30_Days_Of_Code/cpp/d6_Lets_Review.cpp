#include <iostream>
#include <string>
using namespace std;

int main(int argc, char **argv) {
    int T, i = 0;
    cin >> T;
    string S;

    while(i < T) {
        cin >> S;
        unsigned int j = 0;
        string evenS = "", oddS = "";
        while (j < S.length()) {
            j % 2 == 0 ? evenS += S[j] : oddS += S[j];
            ++j;
        }
        cout << evenS << " " << oddS << endl;
        ++i;
    }

    return 0;
}
