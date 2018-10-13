#include<iostream>
#include <utility>
using namespace std;
#define NIL -1

int gcd(int a, int b) {
  if (a>b) {
    swap(a,b);
  }
  int r = b%a;
  while (r!=0) {
    b = a;
    a = r;
    r = b%a;
  }
  return a;
}

int lcm(int a, int b) {
  int c = gcd(a,b);
  return a*b/c;
}

int comp(int N, int M, char S[], char T[]) {
  int c = gcd(N, M);
  int n = N/c;
  int m = M/c;
  int s=0, t=0;
  for (int i=0; i<c; i++) {
    if (S[s]!=T[t]) {
      return NIL;
    }
    s = (i+1)*n;
    t = (i+1)*m;
  }
  return N*M/c;
}

int main() {
  int N, M;
  cin >> N >> M;
  char S[N], T[M];
  for (int i=0; i<N; i++) {
    cin >> S[i];
  }
  for (int i=0; i<M; i++) {
    cin >> T[i];
  }
  int out = comp(N, M, S, T);
  cout << out << endl;

  return 0;
}
