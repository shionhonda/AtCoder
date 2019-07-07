L, R = map(int, input().split())
# 2019 = 3*673
p = 673
if R-L>=p:
    print(0)
else:
    ans = 2019
    for i in range(L,R+1):
        for j in range(i+1,R+1):
            ans = min((i*j)%2019, ans)
    print(ans)
            

