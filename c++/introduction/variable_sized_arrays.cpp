#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int n = 0, q = 0;
    cin >> n >> q;

    vector<int> arr[n];   
    int k = 0;
    int ctr2 = 0;
    // while (ctr2 < n) {
    while(n) {
        cin >> k;
        int ctr = 0;
        // while (ctr < k) {
        while(k) {
            int num;
            cin >> num;
            arr[ctr2].push_back(num);
            ++ctr;
            --k;
        }
        ++ctr2;
        --n;
    }

    int ctr3 = 0;
    while (q) {
        int i = 0, j = 0;
        cin >> i >> j;
        cout << arr[i].at(j);
        cout << endl;
        ++ctr3;
        --q;
    }

    return 0;
}
