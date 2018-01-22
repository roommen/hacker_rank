#include <iostream>
#include <iomanip>

int main(int argc, char **argv) {
    int T;
    std::cin >> T;

    while(T) {
        int A; std::cin >> A;
        double B; std::cin >> B;
        double C; std::cin>> C;

        std::cout << std::hex << "0x" << A << std::endl;

        std::cout << std::dec << std::right << std::setw(15) << std::setfill('_') << std::showpos << std::fixed << std::setprecision(2) << B << std::endl;

        std::cout << std::scientific << std::uppercase << std::noshowpos << std::setprecision(9) << C << std::endl;

        --T;
    }

    return 0;
}
