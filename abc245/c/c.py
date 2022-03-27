def under_num(l, i, k):
    res = set()
    for j in l:
        if abs(j-A[i]) <= k:
            res.add(A[i])
        if abs(j-B[i]) <= k:
            res.add(B[i])
    return list(res)

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
flg = True
t = [A[0], B[0]]
for i in range(1, n):
    t = under_num(t, i, k)
    if not t:
        flg = False
        break
print('Yes' if flg else 'No')

""" official answer
n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2)]
dp = [[False]*n for _ in range(2)]
dp[0][0] = dp[1][0] = True
for i in range(1, n):
    for j in range(2):
        pi = i - 1
        for pj in range(2):
            if not dp[pj][pi]:
                continue
            if abs(A[pj][pi] - A[j][i]) > k:
                continue
            dp[j][i] = True
if dp[0][n-1] or dp[1][n-1]:
    print('Yes')
else:
    print('No')
"""