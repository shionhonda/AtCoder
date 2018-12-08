#include<iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int max = 0;
    int sum = 0;
    int tmp;
    for (int i=0; i<N; i++) {
        cin >> tmp;
        sum += tmp;
        if (tmp > max) {
            max = tmp;
        }
    }
    cout << sum-max/2 << endl;
    return 0;
}