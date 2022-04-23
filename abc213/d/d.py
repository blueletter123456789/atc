import sys
import heapq

sys.setrecursionlimit(1 << 18)

def dfs(current):
    seen[current] = True
    route.append(str(current+1))
    que = al[current].copy()
    heapq.heapify(que)
    while len(que):
        v = heapq.heappop(que)
        if seen[v]:
            continue
        dfs(v)
        route.append(str(current+1))

n = int(input())
al = [list() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
    al[b-1].append(a-1)

seen = [False]*n
route = list()
dfs(0)
print(' '.join(route))


""" sample source

import sys

sys.setrecursionlimit(300000)

n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(n+1):
    G[i].sort()

ans = []
def dfs(crr, pre):
    ans.append(crr)
    for nxt in G[crr]:
        if nxt == pre:
            continue
        dfs(nxt, crr)
    ans.append(crr)
dfs(1, -1)
print(*ans)

"""
