M = 998244353

n, m, k = map(int, input().split())
E = [list() for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    E[u-1].append(v-1)
    E[v-1].append(u-1)

dp = [[0]*n for _ in range(k+1)]
dp[0][0] = 1
for day in range(k):
    num = 0
    for lst in range(n):
        num += dp[day][lst]
    for nxt in range(n):
        dp[day+1][nxt] = (num - dp[day][nxt])
        for lst in E[nxt]:
            dp[day+1][nxt] -= dp[day][lst]
        dp[day+1][nxt] %= M

print(dp[k][0] % M)
