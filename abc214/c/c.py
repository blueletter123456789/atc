# n = int(input())
# S = list(map(int, input().split()))
# T = list(map(int, input().split()))
# dp = [T[i] for i in range(n)]
# lst = list()
# for i in range(n):
#     lst.append((i, S[i], T[i]))
# lst.sort(key=lambda x: x[1]+x[2])
# for i, s, t in lst:
#     dp[(i+1)%n] = min(dp[(i+1)%n], dp[i]+s)
# for ans in dp:
#     print(ans)

n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
dp = [T[i] for i in range(n)]
for i in range(n*2):
    dp[(i+1)%n] = min(dp[(i+1)%n], dp[i%n]+S[i%n])
for ans in dp:
    print(ans)
