import math
from decimal import Decimal

def r_dist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

r, x, y = map(Decimal, input().split())

to_zero = r_dist(x, y, 0, 0)**Decimal("0.5")
if to_zero % r == 0:
    dist = to_zero // r
else:
    dist = (to_zero // r) + 1
    if dist == 1:
        dist += 1

print(-(-dist // 1))
