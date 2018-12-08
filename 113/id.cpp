#include<stdio.h>
#include<vector>
#include<algorithm>
#include<numeric>
#include<math.h>
using namespace std;

int main() {
  int N, M, p, y;
  int A[M], Y[M];
  vector<int> indices(M);
  iota(indices.begin(), indices.end(), 0);
  scanf("%d %d", &N, &M);
  for (int j=0; j<M; j++) {
    scanf("%d %d", &p, &y);
    Y[j] = y;
    A[j] = p*pow(10,9) + y-1; //6+9 = 15 digits
  }

  sort(indices.begin(), indices.end(), [&A](int i, int j) {
        return A[i] < A[j];
  });

  for (int i=0; i<M; i++) {
    int arg = indices[i];
    int tmp = A[arg]/pow(10,9);
    printf("%d\n",  tmp*pow(10,6) + Y[arg]);
  }

  return 0;
}
