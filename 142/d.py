A, B = map(int, input().split())

def factorize(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a

D = gcd(A,B)
factors = factorize(D)
if factors[0][0]==1:
    print(1)
else:
    print(len(factors)+1)