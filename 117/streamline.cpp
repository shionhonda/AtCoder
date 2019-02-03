#include<iostream>
#include<algorithm>
using namespace std;

int main() {
    int n, m, tmp;
    cin >> n >> m;
    int v[m], u[m-1];
    for (int i=0; i<m; i++) {
        cin >> tmp;
        v[i] = tmp;
    }
    if (n>=m) {
        cout << 0 << endl;
        return 0;
    }
    sort(v, v+m); // ascending
    for (int i=0; i<m-1; i++) {
        u[i] = v[i+1] - v[i];
    }
    sort(u, u+m-1); // ascending
    int sum=0;
    for (int i=0; i<m-n; i++) {
        sum += u[i];
    }
    cout << sum << endl;
    return 0;
}