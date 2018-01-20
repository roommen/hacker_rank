#include <iostream>
#include <map>
#include <string>

int main(int argc, char **argv) {
    int Q;
    std::cin >> Q;

    std::map<std::string, int> m;

    while(Q) {
        int q, y;
        std::string x;
        std::cin >> q >> x;
        switch(q) {
            case 1:
                std::cin >> y;
                m[x] += y;
                break;
            case 2:
                m.erase(x);
                break;
            case 3:
                std::cout << (m.find(x)!= m.end() ? m[x] : 0) << std::endl;
                break;
        }
        --Q;
    }

    return 0;
}
