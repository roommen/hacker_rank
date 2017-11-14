#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int N, inp;
    cin >> N;
    vector<int> v;
    // int arr1[1000], arr2[1000];
    // int j = N-1;
    // while (i < N) {
    //     cin >> arr1[i];
    //     arr2[j] = arr1[i];
    //     ++i;
    //     --j;
    // }
    // j = 0;
    // while (j < N) {
    //     cout << arr2[j];
    //     cout << " ";
    //     ++j;
    // }

    // return 0;
    // int j = 0;
    while (N != 0) {
        cin >> inp;
        v.push_back(inp);
        --N;
    }

    for(auto it = v.rbegin(); it != v.rend(); it++) {
        cout << *it << " ";
    }

    return 0;
}
