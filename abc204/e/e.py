from collections import namedtuple
import heapq
import math

INF = 1 << 30

def get_dist(now, c, d):
    to = int(d ** .5) - 1
    res = min(t - now + c + d // (t + 1) for t in [to, to + 1, now] if t >= now)
    # t = max(0, math.ceil(math.sqrt(d))-1-now)
    # res = t + c + d//(t+now+1)
    return res

def solved():
    dist = [INF]*n
    dist[0] = 0
    que = [(0, 0)]

    while len(que):
        cos, u = heapq.heappop(que)
        if cos > dist[u]:
            continue
        for e in G[u]:
            v, c, d = e
            w = get_dist(cos, c, d)
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(que, (dist[v], v))
    
    if dist[n-1] == INF:
        return -1
    else:
        return dist[n-1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = [list() for _ in range(n)]
    Edge = namedtuple('Edge', ['to', 'cost', 'ad'])
    for _ in range(m):
        a, b, c, d = map(int, input().split())
        G[a-1].append(Edge(b-1, c, d))
        G[b-1].append(Edge(a-1, c, d))
    
    print(solved())
    