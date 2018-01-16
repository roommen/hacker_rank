#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int N;
    cin >> N;

    vector<int> vect;
    int n;
    while(N) {
        cin >> n;
        vect.push_back(n);
        --N;
    }

    int x;
    cin >> x;
    vect.erase(vect.begin() + (x-1));

    int a, b;
    cin >> a >> b;

    vect.erase(vect.begin() + (a-1), vect.begin() + (b-1));

    cout << vect.size();
    cout << endl;
    for (int v : vect)
        cout << v << " ";

    return 0;
}
