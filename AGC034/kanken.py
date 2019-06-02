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
    block_cnt = 0
    space_cnt = 0
    if S[D-1]=='.' and S[D+1]=='.':
        space_flg = True
    else: 
        space_flg = False
    for i,s in enumerate(S[A:C+1]):
        if s=='#':
            block_cnt += 1
            if B<=i+A and i+A<D and (not space_flg):
                space_cnt = 0
        else:
            block_cnt = 0
            if B<=i+A and i+A<D and (not space_flg):
                space_cnt += 1
        #print(i+A, block_cnt, space_cnt)
        if block_cnt>=2:
            return 'No'
        if space_cnt>=3:
            space_flg = True
    if space_flg:
        return 'Yes'
    else:
        return 'No'
                


if C<D:
    print(cd())
else:
    print(dc())