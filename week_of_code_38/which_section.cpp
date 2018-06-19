#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char **argv) {
    int t;
    cin >> t;

    int n, k, m;
    while(t > 0) {
        cin >> n >> k >> m;
        vector<int> v;
        int x;
        while(m > 0) {
            cin >> x;
            v.push_back(x);
            --m;
        }
        int ctr = 0;
        int first = 1;
        int second = v[0];
    //    for(auto &x : v) {
        // while()
        for(auto it=v.begin(); it !=v.end(); it++) {
            if ((k >= first) && (k <= second))
            {
                cout << ctr+1 << endl;
                break;
            }
            first = second + 1;
            second = second + v[ctr+1];
            ++ctr;
        }
        --t;
    }

    return 0;
}
