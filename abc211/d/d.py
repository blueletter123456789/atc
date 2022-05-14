from collections import deque

M = 10**9 + 7

n, m = map(int, input().split())
G = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dist = [-1] * n
dp = [0]*n
que = deque([0])
dist[0] = 0
dp[0] = 1
while len(que):
    current = que.popleft()
    for v in G[current]:
        if dist[v] == -1:
            dp[v] = dp[current]
            dist[v] = dist[current]+1
            que.append(v)
        elif dist[v] == dist[current]+1:
            dp[v] += dp[current]
            dp[v] %= M

print(dp[n-1]%M)

# TLE source cord
# from collections import deque
# import sys

# M = 1 << 30
# sys.setrecursionlimit(M)

# n, m = map(int, input().split())
# G = [list() for _ in range(n)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     G[a-1].append(b-1)
#     G[b-1].append(a-1)
# INF = 1 << 30
# dist = [INF] * n

# que = deque([0])
# dist[0] = 0
# while len(que):
#     current = que.popleft()
#     for v in G[current]:
#         if dist[v] < dist[current]+1:
#             continue
#         dist[v] = dist[current]+1
#         que.append(v)

# def dfs(current):
#     if current == 0:
#         return 1
#     res = 0
#     for v in G[current]:
#         if dist[current] - dist[v] != 1:
#             continue
#         res += dfs(v)
#     return res

# print(dfs(n-1)%M)
