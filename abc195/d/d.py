n, m, q = map(int, input().split())

N = list()
for _ in range(n):
    w, v = map(int, input().split())
    N.append((v, w))
N.sort(reverse=True)

M = list()
for i in map(int, input().split()):
    M.append(i)

for _ in range(q):

    l, r = map(int, input().split())

    total_val = 0

    used = [False]*m
    
    for i, val in enumerate(N):
        v, w = val
        max_size, max_idx = float('inf'), -1
        for j, lim in enumerate(M):
            if j+1 >= l and j+1 <= r:
                continue
            if w <= lim and not used[j] and max_size > lim:
                max_size = lim
                max_idx = j
        
        if max_idx >= 0:
            used[max_idx] = True
            total_val += v
    
    print(total_val)



# WE source code.
# class SegmentTreeRMQ(object):

#     def __init__(self, length):
#         self.n = 1
#         self.dat = list()
#         self.length = length

#         while self.n < length:
#             self.n *= 2
        
#         self.dat = [float('inf')]*(2 * self.n - 1)
    
#     def update(self, k, a):
#         k += self.n - 1
#         self.dat[k] = a

#         while k > 0:
#             k = (k - 1) // 2
#             self.dat[k] = min(self.dat[k*2+1], self.dat[k*2+2])
    
#     def query(self, a, b):
#         l = k = 0
#         r = self.n
#         def _query(a, b, k, l, r):
#             if r <= a or b <= l:
#                 return float('inf')
            
#             if a <= l and r <= b:
#                 return self.dat[k]
#             else:
#                 vl = _query(a, b, k*2+1, l, (l+r)//2)
#                 vr = _query(a, b, k*2+2, (l+r)//2, r)
#                 return min(vl, vr)
#         return _query(a, b, k, l, r)


# n, m, q = map(int, input().split())
# N = list()
# for _ in range(n):
#     w, v = map(int, input().split())
#     N.append((w, v))
# M = [i for i in map(int, input().split())]

# dp = [[-float('inf') for _ in range(10**6 + 1)] for _ in range(m+1)]
# st = SegmentTreeRMQ(n)

# for i in range(m):
#     dp[i][0] = 0
#     max_num = -float('inf')
#     for k in range(n):
#         for j in range(M[i]+1):
#             if j < N[k][0]:
#                 continue
#             dp[i+1][j] = max(dp[i+1][j], dp[i][j-N[k][0]]+N[k][1])
#         max_num = max(max_num, dp[i+1][j])
#     st.update(i, -max_num)

# for _ in range(q):
#     l, r = map(int, input().split())
#     print(-st.query(l, r))

