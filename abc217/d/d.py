""" TLE source code
import bisect

l, q = map(int, input().split())
block = [0, l]
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        bisect.insort(block, x)
    else:
        idx = bisect.bisect_left(block, x)
        print(block[idx]-block[idx-1])
"""

