import numpy as np

def binary_array(x, max_len):
    x = bin(x)[2:]
    x = '0' * (max_len - len(x)) + x
    return [int(a) for a in list(x)]

def main():
    n, k = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    if k==0:
        print(sum(a))
        return
    
    max_len = max(len(bin(max(a))), len(bin(k))) - 2
    A = [binary_array(aa, max_len) for aa in a]
    A = np.array(A)
    k_array = np.array(binary_array(k, max_len))

    s = []
    K = 0
    for i in range(len(k_array)):
        K += 2**(max_len-1-i)
        if K<=k:
            tmp = np.sum(A[:,i])
            s.append(max(tmp, n-tmp))
        else:
            s.append(np.sum(A[:,i]))
            K -= 2**(max_len-1-i)
        

    ans = 0
    for i,ss in enumerate(s):
        ans += 2**(max_len-1-i) * ss
    print(ans)



if __name__=='__main__':
    main()