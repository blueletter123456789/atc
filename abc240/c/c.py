n, x = map(int, input().split())
dp = [[False]*(x+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(1, n+1):
    a, b = map(int, input().split())
    for j in range(0, x+1):
        if a <= j and not dp[i][j]:
            dp[i][j] = dp[i-1][j-a]
        if b <= j and not dp[i][j]:
            dp[i][j] = dp[i-1][j-b]
if dp[n][x]:
    print('Yes')
else:
    print('No')
