X, Y = map(int, input().split())
MAX = 10**9+7

def cmb(n, r, mod, g1, g2):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod



def main(X, Y):
    _X = 2*X - Y
    _Y = -X + 2*Y
    if _X%3!=0 or _Y%3!=0:
        return 0

    X = _X//3
    Y = _Y//3

    mod = 10**9+7 #出力の制限
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range( 2, X+Y + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )

    return cmb(X+Y, X, MAX, g1, g2)

print(main(X, Y)%MAX)