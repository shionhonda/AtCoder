#include<iostream>
using namespace std;

int N, K;


int main(){
  int cnt = 0;
  int a, b, c;
  cin >> N >> K;

  for (int m=1; m*K<3*N; m++) {
    for (a=1; a<m*K/3.0; a++) {
      if ((b+c)%K!=0){
        continue;
      }
      for (b=a; b<(m*K-a)/2.0; b++) {
        if ((a+b)%K!=0){
          continue;
        }
        c = m*K-a-b;
        if ((c+a)%K!=0)
      }
    }
  }
}
