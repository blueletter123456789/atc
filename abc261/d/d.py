n, m = map(int, input().split())
X = list(map(int, input().split()))
b = dict()
for _ in range(m):
    c, y = map(int, input().split())
    b[c] = y

# i回目のコイントスが終わった時点でのカウンタの数値に対する最大値
dp = [[-1]*(n+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        # i > 0の場合はコインの表が出た場合のみ
        dp[i][j] = dp[i-1][j-1] + X[i-1] + b.get(j, 0)
    
    dp[i][0] = 0
    for j in range(i):
        # コインの裏が出た場合にどこから遷移したかの最大値を取る
        dp[i][0] = max(dp[i][0], dp[i-1][j])

ans = 0
for i in range(n+1):
    ans = max(ans, dp[n][i])

print(ans)


# TLE Source code
# import sys

# sys.setrecursionlimit(10000)


# def dfs(cur, cost, cnt):
#     if cnt > n:
#         return cost
    
#     memo[cnt][cur] = cost
#     res = 0
#     for v, p in G[cur]:
#         if memo[cnt+1][v] > cost+p:
#             continue
#         res = max(res, dfs(v, cost+p, cnt+1))
#     return res


# n, m = map(int, input().split())
# X = list(map(int, input().split()))
# C = dict()
# for i in range(m):
#     c, y = map(int, input().split())
#     C[c] = y

# G = [list() for _ in range(n+1)]
# for i in range(n):
#     G[i].append((0, 0))
#     if i+1 in C:
#         G[i].append((i+1, X[i]+C[i+1]))
#     else:
#         G[i].append((i+1, X[i]))

# memo = [[0]*(n+1) for _ in range(n+2)]

# print(dfs(0, 0, 0))
