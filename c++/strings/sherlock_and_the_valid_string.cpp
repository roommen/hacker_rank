#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(int argc, char **argv) {
    string str;
    cin >> str;

    map<char, int> strCtr;
    for (char s: str) {
        if (strCtr.find(s) != strCtr.end()) {
            int ctr = strCtr[s];
            strCtr[s] = ++ctr;
        }
        else
            strCtr[s] = 1;
    }

    int gt = 0, lt = 0, ctr = -1;
    for (auto it=strCtr.begin(); it!=strCtr.end(); ++it) {
        if(ctr != -1) {
            if (ctr < it->second)
                ++lt;
            if (ctr > it->second)
                ++gt;
        }
        else {
            ctr = it->second;
        }
    }

    if (lt == 0 && gt == 0)
        cout << "YES" << endl;
    else if((gt == 1 && lt == 0) || (gt == 0 && lt == 1))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    return 0;
}
