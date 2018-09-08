#include<iostream>
using namespace std;

int main() {
  int k;
  cin >> k;
  if (k%2==0) {
    cout << k*k/4 << endl;
  } else {
    cout << (k-1)*(k+1)/4 << endl;
  }
  return 0;
}
