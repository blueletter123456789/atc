from collections import deque

n, x = map(int, input().split())

dist = [[0, 0, 0] for _ in range(n+1)]
for i in range(1, n+1):
    a, b = map(int, input().split())
    dist[i][0] = a + b + dist[i-1][0]
    if x - i > 0:
        dist[i][1] = b * (x-i) + dist[i][0]
    else:
        dist[i][1] = dist[i][0]

ans = 10 ** 19
for i in range(1, n+1):
    ans = min(ans, dist[i][1])

print(ans)
