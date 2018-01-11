#include <iostream>
using namespace std;

int factorial(int num) {
    if (num == 0)
        return 1;
    return num * factorial(num-1);
}


int main(int argc, char **argv) {
    int N;
    cin >> N;
    cout << factorial(N);

    return 0;
}
