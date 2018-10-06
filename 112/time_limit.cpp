#include<iostream>
using namespace std;
int arg=101;
int cost=1001;


int main() {
  int N, T, c, t;
  cin >> N >> T;
  for (int i=0; i<N; i++) {
    cin >> c >> t;
    if (t<=T) {
      if (c<cost) {
        cost = c;
        arg = i;
      }
    }
  }
  if (cost==1001) {
    cout << "TLE" << endl;
  } else {
    cout << cost << endl;
  }
  return 0;
}
