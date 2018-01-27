#include <iostream>

using std::cout;
using std::cin;

class Rectangle {
public:
    int width, height;
    void display() {
        cout << width << " " << height << std::endl;
    }
};

class RectangleArea : public Rectangle {
public:
    void read_input() {
        cin >> Rectangle::width >> Rectangle::height;
    }
    void display() {
        cout << width * height << std::endl;
    }
};

int main()
{
    /*
     * Declare a RectangleArea object
     */
    RectangleArea r_area;

    /*
     * Read the width and height
     */
    r_area.read_input();

    /*
     * Print the width and height
     */
    r_area.Rectangle::display();

    /*
     * Print the area
     */
    r_area.display();

    return 0;
} 
