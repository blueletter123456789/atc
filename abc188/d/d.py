N, C = map(int, input().split())
event = []
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    # 0-indexに修正する[a, b)
    event.append((a, c))
    event.append((b, -c))

event.sort()
ans = 0
fee = 0
t = 0
for x, y in event:
    # eventの開始が異なる時に経過分を計算
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y

print(ans)


# from collections import defaultdict

# class BIT(object):

#     def __init__(self, n):
#         self.bit0 = defaultdict(int)
#         self.bit1 = defaultdict(int)
#         self.n = n
    
#     def add(self, b, i, v):
#         while i <= self.n:
#             b[i] += v
#             i += (i & -i)
    
#     def sum(self, b, i):
#         s = 0
#         while i > 0:
#             s += b.get(i, 0)
#             i -= (i & -i)
#         return s


# n, c = map(int, input().split())

# l = [0]*n
# r = [0]*n
# w = [0]*n

# st, en = float('inf'), 0
# for i in range(n):
#     l[i], r[i], w[i] = map(int, input().split())
#     st = min(st, l[i])
#     en = max(en, r[i])

# bt = BIT(en+1)
# for x, y, z in zip(l, r, w):
#     res = 0
#     res += bt.sum(bt.bit0, y) + bt.sum(bt.bit1, y)*y
#     res -= bt.sum(bt.bit0, x-1) + bt.sum(bt.bit1, x-1)*(x-1)

#     if res + z*(y-x) <= c*(y-x):
#         bt.add(bt.bit0, x, -z*(x - 1))
#         bt.add(bt.bit1, x, z)
#         bt.add(bt.bit0, y+1, z*y)
#         bt.add(bt.bit1, y+1, -z)
#     else:
#         res = res / (y-x+1)
#         bt.add(bt.bit0, x, res*(x - 1))
#         bt.add(bt.bit0, x, -c*(x - 1))
#         bt.add(bt.bit1, x, -res)
#         bt.add(bt.bit1, x, c)
#         bt.add(bt.bit0, y+1, -res*y)
#         bt.add(bt.bit0, y+1, c*y)
#         bt.add(bt.bit1, y+1, res)
#         bt.add(bt.bit1, y+1, -c)

# ans = 0
# ans += bt.sum(bt.bit0, en) + bt.sum(bt.bit1, en)*en
# ans -= bt.sum(bt.bit0, st-1) + bt.sum(bt.bit1, st-1)*(st-1)
# print(int(ans))
