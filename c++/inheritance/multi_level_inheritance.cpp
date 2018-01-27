#include <iostream>

using std::cout;
using std::cin;

class Triangle {
public:
    void triangle() {
        cout << "I am a triangle" << std::endl;
    }
};

class Isosceles : public Triangle {
public:
    void isosceles() {
        cout << "I am an isoscles triangle" << std::endl;
    }
};

class Equilateral : public Isosceles {
public:
    void equilateral() {
        cout << "I am an equilateral triangle" << std::endl;
    }
};


int main(int argc, char **argv) {
    Equilateral eqr;
    eqr.equilateral();
    eqr.isosceles();
    eqr.triangle();

    return 0;
}

