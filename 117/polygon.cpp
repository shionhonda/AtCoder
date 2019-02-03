#include<iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int sum=0, max=0;
    int tmp;
    for (int i=0; i<n; i++) {
        cin >> tmp;
        sum += tmp;
        if (tmp>max) {
            max = tmp;
        }
    }
    if (sum>2*max) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}