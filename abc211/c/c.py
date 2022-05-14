M = 10**9 + 7

s = input()
t = 'chokudai'
dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
for i in range(len(s)+1):
    dp[0][i] = 1

for i in range(len(t)):
    for j in range(len(s)):
        if i > j:
            dp[i+1][j+1] = dp[i+1][j]
            continue
        if t[i] == s[j]:
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j]
        else:
            dp[i+1][j+1] = dp[i+1][j]
        dp[i+1][j+1]%M
print(dp[len(t)][len(s)]%M)
