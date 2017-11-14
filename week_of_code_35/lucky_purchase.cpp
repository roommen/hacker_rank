#include <iostream>
#include <string>
using namespace std;

int main(int argc, char **argv) {
    unsigned long int n;
    cin >> n;

    string name = "";
    long long int price = -1, low_price = 10000000001;
    string low_price_name = "-1";

    while (n > 0) {
        cin >> name >> price;
        unsigned int no4 = 0, no7 = 0;
        for (char p: to_string(price)){
            if (p == '7')
                no7 += 1;
            if (p == '4')
                no4 += 1;
        }
        if (no7 > 0 && no4 > 0) {
            if (no7 == no4) {
               if (price < low_price) {
                    low_price = price;
                    low_price_name = name;
                }
            }
        }
        --n;
    }

    cout << low_price_name << endl;
    return 0;
}
