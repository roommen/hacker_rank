#include <iostream>

int main(int argc, char **argv) {
    int q = 0;
    std::cin >> q;

    while (q > 0) {
        std::string name;
        std::cin >> name;

        if((name.substr(0,5) == "hydro") && (name.substr(name.length() - 2) == "ic"))
            std::cout << "non-metal acid" << std::endl;
        else if ((name.substr(0,5) != "hydro") && (name.substr(name.length() - 2) == "ic"))
            std::cout << "polyatomic acid" << std::endl;
        else
            std::cout << "not an acid" << std::endl;
        --q;
    }

    return 0;
}