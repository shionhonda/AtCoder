#include<iostream>
using namespace std;

int main() {
    int n, h, w, cnt=0;
    cin >> n >> h >> w;
    for (int i=0; i<n; i++) {
        int a, b;
        cin >> a >> b;
        if (a>=h && b>=w) {
            cnt += 1;
        }
    }
    cout << cnt << endl;
    return 0;
}