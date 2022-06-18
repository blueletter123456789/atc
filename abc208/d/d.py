INF = 10**9

n, m = map(int, input().split())
dp = [[[INF]*(n) for _ in range(n)] for _ in range(2)]
prev, nxt = 0, 1
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dp[prev][a][b] = c

for i in range(n):
    dp[prev][i][i] = 0

ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[nxt][i][j] = min(dp[prev][i][j], dp[prev][i][k] + dp[prev][k][j])
            if dp[nxt][i][j] < INF:
                ans += dp[nxt][i][j]
    prev, nxt = nxt, prev

print(ans)
