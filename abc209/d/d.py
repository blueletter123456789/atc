from collections import deque

n, q = map(int, input().split())
al = [list() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    al[a-1].append(b-1)
    al[b-1].append(a-1)

INF = 10**6
dist = [INF]*n
que = deque([0])
dist[0] = 0
while len(que):
    current = que.popleft()
    for v in al[current]:
        if dist[v] != INF:
            continue
        dist[v] = dist[current] + 1
        que.append(v)

for _ in range(q):
    c, d = map(int, input().split())
    if abs(dist[c-1] - dist[d-1]) % 2:
        print('Road')
    else:
        print('Town')
