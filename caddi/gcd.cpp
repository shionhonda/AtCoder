#include<iostream>
#include<math.h>
using namespace std;

long euclid(long a, long b) {
    if (a<b) {
        long tmp = a;
        a = b;
        b = tmp;
    }
    if (b==0) {
        return a;
    }
    long r = a % b;
    while (r!=0) {
        a = b;
        b = r;
        r = a % b;
    } 
  return b;
}

long devide(long N, int nn, long P) {
    long m = ceil(sqrt(P));
    long gcd=0, p=P, q=1;
    for (long i=m; i>0; i--){
        if (P%i==0) {
            long j = P/i;
            long tmp = euclid(j, i);
            if (tmp>gcd) {
                gcd = tmp;
                p = j;
                q = i;
            }
        }
    }
    cout << nn << " " << gcd << " " << p << " " << q << endl;
    if (pow(2, nn)>=N) {
        if (gcd==1) {
            return 0;
        }
        return gcd;
    }
    long g1 = devide(N, nn+1, p);
    long g2 = devide(N, nn+1, q);
    return ;
}

int main() {
    long N, P;
    cin >> N >> P;
    devide(N, 1, P);
    //cout << devide(n) << endl;
    return 0;
}