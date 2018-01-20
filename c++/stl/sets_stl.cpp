#include <iostream>
#include <set>

int main(int argc, char **argv) {
    std::set<int> s;
    int Q;
    std::cin >> Q;

    while(Q) {
        int x = 0, y = 0;
        std::cin >> y >> x;

        switch(y) {
            case 1:
                s.insert(x);
                break;
            case 2:
                s.erase(x);
                break;
            case 3:
                std::cout << (s.find(x) != s.end() ? "Yes" : "No") << std::endl;
                break;
        }
        --Q;
    }

    return 0;
}
