S = list(map(int, input().split('/')))

def main():
    if S[0]>2019:
        print('TBD')
        return
    elif S[0]==2019 and S[1]>4:
        print('TBD')
        return
    else:
        print('Heisei')
        return 

main()
    