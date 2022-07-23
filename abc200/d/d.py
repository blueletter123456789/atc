from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

seen = defaultdict(list)
for i in range(1, 1 << n):
    if i > 201:
        break
    num = 0
    nums = list()
    for j in range(n):
        if i & (1 << j):
            num += A[j]
            nums.append(str(j+1))
    seen[num%200].append(nums)

ans = -1
for k, row in seen.items():
    if len(row) < 2:
        continue
    ans = k
    break

if ans < 0:
    print('No')
else:
    print('Yes')
    print(len(seen[ans][0]), ' '.join(seen[ans][0]))
    print(len(seen[ans][1]), ' '.join(seen[ans][1]))


# n = int(input())
# A = list(map(int, input().split()))

# dp = list()
# for _ in range(n+1):
#     row = [[] for _ in range(201)]
#     dp.append(row)

# dp[0][0].append(0)
# for i in range(n):
#     for j in range(201):
#         dp[i+1][j] = dp[i][j].copy()
#         if dp[i][(j-A[i])%200]:
#             dp[i+1][j].append(dp[i][(j-A[i])%200][0] | 1 << i)

# ans = -1
# for i, row in enumerate(dp[n]):
#     if len(row) < 2:
#         continue
#     ans = i
#     break

# if ans < 0:
#     print('No')
# else:
#     ans1 = list()
#     for i in range(n):
#         if dp[n][ans][0] & (1 << i):
#             ans1.append(str(i+1))
    
#     ans2 = list()
#     for j in range(n):
#         if dp[n][ans][1] & (1 << j):
#             ans2.append(str(j+1))
#     print('Yes')
#     print(len(ans1), ' '.join(ans1))
#     print(len(ans2), ' '.join(ans2))

