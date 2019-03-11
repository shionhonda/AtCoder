A, B = map(int, input().split())

def main():
    d = B-A
    if d==0:
        return A
    elif d==1:
        return A^B
    elif A%2==1:
        if B%2==1:
            if d%4==0:
                return A
            else:
                return A^1
        else:
            if d%4==1:
                return A^B
            else:
                return A^1^B
    else:
        if B%2==1:
            if d%4==1:
                return 1
            else:
                return 0
        else:
            if d%4==0:
                return B
            else:
                return 1^B

print(main())