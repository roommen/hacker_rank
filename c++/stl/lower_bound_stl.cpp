#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int N;
    cin >> N;

    vector<int> vect;
    int x;
    while (N) {
        cin >> x;
        vect.push_back(x);
        --N;
    }

    int Q;
    cin >> Q;
    while (Q) {
        int y;
        cin >> y;
        vector<int>::iterator low = lower_bound(vect.begin(), vect.end(), y);
        int pos = low - vect.begin();
        if (pos < vect.size())
            cout << "Yes " << pos+1;
        else {
            ++y;
            int last = vect.at(vect.size() - 1);
            low = lower_bound(vect.begin(), vect.end(), y);
            pos = low - vect.begin();
            while((y < last) && (pos != vect.size())) {
                ++y;
                low = lower_bound(vect.begin(), vect.end(), y);
                pos = low - vect.begin();
            }
            cout << "No " << pos + 1;
        }
        --Q;
    }
    return 0;
}