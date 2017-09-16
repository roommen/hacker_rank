#include <iostream>

using namespace std;

int main()
{
    int num;
    cin >> num;

    if (num %2 != 0)
        cout << "Weird" << endl;
    else
    {
        if (num >= 2 and num <= 5)
            cout << "Not Weird" << endl;
        else if(num >= 6 && num <= 20)
            cout << "Weird";
        else if (num > 20)
            cout << "Not Weird";
    }
    return 0;
}