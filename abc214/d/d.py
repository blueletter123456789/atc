# import heapq
# import sys

# INF = sys.maxsize

# n = int(input())
# al = [list() for _ in range(n)]
# for _ in range(n-1):
#     u, v, w = map(int, input().split())
#     al[u-1].append((v-1, w))

# dist = [INF]*n
# dist[0] = 0
# ans = [[-1]*n for _ in range(n)]
# que = [(dist[0],0)]
# heapq.heapify(que)
# while len(que):
#     cur_dist, cur_v = heapq.heappop(que)
#     if cur_dist > dist[cur_v]:
#         continue
#     for v, weight in al[cur_v]:
#         tmp_dis = dist[cur_v] + weight
#         if dist[v] > tmp_dis:
#             dist[v] = tmp_dis
#             heapq.heappush(que, (tmp_dis, v))

# for k, v in enumerate(dist):
#     print(f'{k}: {v}' if v < INF else f'{k}: INF')

class UnionFind(object):
    def __init__(self, length):
        self.par = [-1] * length
        self.size = [1] * length
    
    def root(self, a):
        if self.par[a] == -1:
            return a
        self.par[a] = self.root(self.par[a])
        return self.par[a]
    
    def is_same(self, a, b):
        return self.root(a) == self.root(b)
    
    def unite(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b:
            return False
        if self.uni_size(a) < self.uni_size(b):
            a, b = b, a
        self.par[b] = a
        self.size[a] += self.size[b]
        return True
    
    def uni_size(self, a):
        return self.size[self.root(a)]

n = int(input())
al = list()
for _ in range(n-1):
    u, v, w = map(int, input().split())
    al.append((w, u-1, v-1))
al.sort()
uni = UnionFind(n)
ans = 0
for i in range(n-1):
    w, u, v = al[i]
    u_size = uni.uni_size(u)
    v_size = uni.uni_size(v)
    ans += u_size*v_size*w
    uni.unite(u, v)
print(ans)
