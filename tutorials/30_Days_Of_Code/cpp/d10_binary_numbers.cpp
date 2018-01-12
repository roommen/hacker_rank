#include <iostream>
#include <bitset>
using namespace std;

int main(int argc, char **argv) {
    int num;
    cin >> num;

    string bin = bitset<260>(num).to_string();
    cout << bin;

    int ctr = 0, big = 0;
    for (char c : bin) {
        if (c == '1')
            ++ctr;
        else {
            if (ctr > big)
                big = ctr;
            ctr = 0;
        }
    }
    cout << big;

    return 0;
}
