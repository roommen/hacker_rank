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
        for(auto &x : v) {
            // second = v[ctr];
            cout << "first " << first << " second " << second << endl;
            if ((k >= first) && (k <= second))
            {
                cout << ctr << endl;
                break;
            }
            first = second + 1;
            ++ctr;
            second = v[ctr] + x;
            // second = 
            
        }

        --t;
    }

    return 0;
}
