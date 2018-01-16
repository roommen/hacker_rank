#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int N;
    cin >> N;
    vector<int> vect;
    
    while (N) {
        int e;
        cin >> e;
        vect.push_back(e);
        --N;
    }
    
    sort(vect.begin(), vect.end());
    
    for (int v : vect) {
        cout << v << " ";
    }
    
    return 0;
}