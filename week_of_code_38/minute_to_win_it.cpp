#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char **argv) {
    int n, k;
    cin >> n >> k;

    vector<int> v;
    int x;
    while(n!=0) {
        cin >> x;
        v.push_back(x);
        --n;
    }

    int ctr = 0, chk_sum = 0, sec = 0;
    auto iter = v.begin();
    while(iter != v.end()) {
        chk_sum = *iter + k;
        if(chk_sum != v[ctr+1]) {
            v[ctr+1] = chk_sum;
            ++sec;
        }
        ++ctr;
        ++iter;
    }
    cout << --sec << endl;
    return 0;
}
