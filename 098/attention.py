N = int(input())
S = input()

e_cnt, w_cnt = 0, 0
e_arr, w_arr = [0]*(N+1), [0]*(N+1)
for i,s in enumerate(S):
    if s=='E':
        e_cnt += 1
    else:
        w_cnt += 1
    e_arr[i+1] = e_cnt
    w_arr[i+1] = w_cnt

max_ew = -1e6
for i in range(N):
    max_ew =  max(e_arr[i] - w_arr[i+1], max_ew)
print(N - 1 - (max_ew+w_cnt))