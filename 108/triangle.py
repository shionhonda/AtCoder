N, K = map(int, input().split())

def main():
    a = (N//K)**3
    if K%2!=0:
        print(a)
        return
    else:
        b = ( (N+(K//2)) // K ) **3
        print(a+b)
        return

main() 

