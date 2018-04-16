#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
    private:
    vector<int> elements;
  
  	public:
  	int maximumDifference;

    Difference(vector<int> &a) {
        this->elements = a;
    }

    void computeDifference() {
        int smallest_element = *min_element(elements.begin(), elements.end());
        int largest_element  = *max_element(elements.begin(), elements.end());
        maximumDifference = abs(largest_element - smallest_element);
    }
};

int main() {
    int N;
    cin >> N;
    
    vector<int> a;
    
    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;
        
        a.push_back(e);
    }

    Difference d(a);

    d.computeDifference();

    cout << d.maximumDifference;

    return 0;
}
