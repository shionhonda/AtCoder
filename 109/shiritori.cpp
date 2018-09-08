#include<stdio.h>
#include<cstring>
using namespace std;
#define MAX 100

char List[MAX][10+1];

int judge(char w1[], char w2[], int n) {
  if (w1[strlen(w1)-1]!=w2[0]) {
    return 1;
  } else {
    for (int j=0; j<n; j++){
      if (strcmp(w2, List[j])==0) {
        return 1;
      }
    }
    return 0;
  }
}

int main() {
  int N, cnt=0;
  scanf("%d", &N);
  char w1[10+1], w2[10+1];
  scanf("%s", w1);
  strcpy(List[0], w1);
  for (int i=1; i<N; i++) {
    scanf("%s", w2);
    cnt += judge(w1, w2, i);
    strcpy(List[i], w2);
    strcpy(w1, w2);
  }
  if (cnt>0) {
    printf("No\n");
  } else {
    printf("Yes\n");
  }
  return 0;
}
