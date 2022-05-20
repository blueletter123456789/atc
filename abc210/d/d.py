# wrong answer
# h, w, c = map(int, input().split())

# in_lst = list()
# num_list = [0]*(h*w)

# for i in range(h):
#     row = list(map(int, input().split()))
#     in_lst.append(row)
#     for j in range(w):
#         idx = i*w + j
#         num_list[idx] = (in_lst[i][j], i, j)

# num_list.sort(key=lambda x: (x[0], x[1]+x[2]))
# ans = 1 << 30
# for i in range(h*w):
#     v1, x1, y1 = num_list[i]
#     mem = ans
#     for j in range(i+1, h*w):
#         v2, x2, y2 = num_list[j]
#         ans = min(ans, v1+v2 + (abs(x1-x2)+abs(y1-y2))*c)
#     if mem == ans:
#         break
# print(ans)

h, w, c = map(int, input().split())
in_lst = [list(), list()]
for _ in range(h):
    row = list(map(int, input().split()))
    in_lst[0].append(row)
    in_lst[1].append(list(reversed(row)))

INF = 1 << 60
ans = INF
for k in range(2):
    dp = [[INF]*(w+1) for _ in range(h+1)]
    for i in range(h):
        for j in range(w):
            dp[i+1][j+1] = min(in_lst[k][i][j], dp[i][j+1]+c, dp[i+1][j]+c)
            ans = min(ans, dp[i][j+1]+c+in_lst[k][i][j], dp[i+1][j]+c+in_lst[k][i][j])

print(ans)        
