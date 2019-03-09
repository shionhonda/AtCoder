A, B = map(int, input().split())

st = 1
while st<B:
    st*=2
st = st//2


ans = 0
cur = st
while cur>=1:
    if B-cur<A:
        cur = cur//2
        continue
    else:
        if (B-cur)%2==0:
            ans += cur
            B -= cur
        cur = cur//2

print(ans)