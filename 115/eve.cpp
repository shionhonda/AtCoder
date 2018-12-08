#include<vector>
#include<algorithm>
using namespace std;
#define MAX 1000000000

int main(){
    int N, K;
    scanf("%d %d", &N, &K);
    vector<int> v;
    for (int i=0; i<N; i++) {
        int tmp;
        scanf("%d", &tmp);
        v.push_back(tmp);
    }

    sort(v.begin(), v.end());

    int L=N-K+1, m=MAX;
    for (int i=0; i<L; i++) {
        int tmp = v[K-1+i] - v[i];
        if (tmp<m) {
            m = tmp;
        }
    }
    printf("%d\n", m);
    return 0;
}