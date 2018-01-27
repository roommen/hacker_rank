#include <iostream>

using std::cout;

class Triangle {
public:
    void triangle() {
        cout << "I am a triangle";
    }
};

class Isosceles : public Triangle {
public:
    void isoscles() {
        cout << "I am an isoscles triangle\n";
    }
    void description() {
        cout << "In an isosceles triangle two sides are equal\n";
    }
};

int main(int argc, char **argv) {
    Isosceles isc;
    isc.isoscles();
    isc.description();
    isc.triangle();

    return 0;
}
