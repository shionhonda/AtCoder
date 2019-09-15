N = int(input())
S = input()

def z_algorithm(s):
    l = len(s)
    A = [0]*l
    A[0] = 0
    j = 0
    for i in range(1,l):
        while i+j<l and s[j]==s[i+j]:
            j += 1
        if j<1:
            continue
        A[i] = j
        k = 1
        while k < l-i and k < j-A[k]:
            A[i+k] = A[k]
            k += 1
        i += k
        j -= k
    #print(A, s)
    return A


def main():
    ans = 0
    for i in range(0, N):
        tmp = max(z_algorithm(S[i:]))
        #print(tmp)
        ans = max(ans, tmp)
    print(ans)

main()
