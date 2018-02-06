#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char **argv) {
    int n;
    cin >> n;

    std::vector<int> door;
    int max_door = 0;
    while (n != 0) {
        int d = 0;
        cin >> d;
        door.push_back(d);
        if (d == 1)
            ++max_door;
        --n;
    }

    int min_door = 0;
    for (std::vector<int>::iterator it = door.begin(); it != door.end(); ++it) {
        if ((*it == 1) && (*(it+1) == 0))
            ++min_door;
            
        if ((*it == 1) && (*(it+1) == 1)) {
            ++min_door;
            ++it;
        }
    }

    cout << min_door << " " << max_door;

    return 0;
}
