n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

S = [[0]*(n+1) for _ in range(n+1)]
lim = (k**2)//2 + 1

ng, ok = -1, 10**15
while ng + 1 < ok:
    mid = (ng + ok) // 2
    # 二次元累積和を初期化
    for i in range(n):
        for j in range(n):
            S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j]
            if A[i][j] > mid:
                S[i+1][j+1] += 1
    
    ext = False
    for i in range(n-k+1):
        for j in range(n-k+1):
            part_sum = S[i+k][j+k] + S[i][j] - S[i][j+k] - S[i+k][j]
            if part_sum < lim:
                ext = True
    
    if ext:
        ok = mid
    else:
        ng = mid

print(ok)



# TLE source code
# n, k = map(int, input().split())

# lst = [list(map(int, input().split())) for _ in range(n)]
# ans = 10**15
# mid_idx = (k**2) // 2
# for i in range(n-k+1):
#     for j in range(n-k+1):
#         mid = list()
#         for a in range(i, i+k):
#             for b in range(j, j+k):
#                 mid.append(lst[a][b])
#         mid.sort(reverse=True)
#         ans = min(ans, mid[mid_idx])

# print(ans)
