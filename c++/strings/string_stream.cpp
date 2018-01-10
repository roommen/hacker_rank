#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

vector<int> parseInts(string str) {
    stringstream ss(str);
    int num;
    vector<int> vint;
    char ch;

   while(ss >> num) {
       vint.push_back(num);
       ss >> ch;
   }
   return vint;
}

int main(int argc, char **argv) {
    string str;
    cin >> str;
    vector<int> nums = parseInts(str);
    for (int i = 0; i < nums.size(); ++i)
        cout << nums[i]<<endl;

    return 0;
}