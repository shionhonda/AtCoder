N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
battled = [False]*N
num_games = N*(N-1)//2
cnt_games = 0
num_days = 0
i = 0
while cnt_games<num_games:
    for j in range(N):
        if not battled[j]:
            opp = A[i]
            if A[opp-1]-1 == j:
                cnt_games += 1
                battled[j] = True
                battled[opp-1] = True
            else:
                continue
        else:
            continue
    cnt_games += 1