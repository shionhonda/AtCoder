N, A, B, C, D = map(int, input().split())
S = list(input())
A -= 1
B -= 1
C -= 1
D -= 1

def cd():
    two_block_flg = False
    for s in S[A:C+1]:
        if two_block_flg:
            if s=='#':
                return 'No'
            else:
                two_block_flg = False
        else:
            if s=='#':
                two_block_flg = True
    two_block_flg = False
    for s in S[B:D+1]:
        if two_block_flg:
            if s=='#':
                return 'No'
            else:
                two_block_flg = False
        else:
            if s=='#':
                two_block_flg = True
    return 'Yes'

def dc():
    two_block_flg = False
    for s in S[A:C+1]:
        if two_block_flg:
            if s=='#':
                return 'No'
            else:
                two_block_flg = False
        else:
            if s=='#':
                two_block_flg = True
    for i in range(B, D+1):
        if S[i-1]=='.' and S[i]=='.' and S[i+1]=='.':
            return 'Yes'
    return 'No'  


if C<D:
    print(cd())
else:
    print(dc())