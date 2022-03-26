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

import random
import bisect

def randomized_quicksort(a, left, right):
    if left < right:
        r = random.randint(left, right)
        a[r], a[left] = a[left], a[r]
        p = left
        k = left + 1
        while k <= right:
            if a[k] < a[left]:
                a[p + 1], a[k] = a[k], a[p + 1]
                p += 1
            k += 1
        a[left], a[p] = a[p], a[left]
        a = randomized_quicksort(a, left, p - 1)
        a = randomized_quicksort(a, p + 1, right)
    return a

l, q = map(int, input().split())
block = [0, l]
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        block.append(x)
    else:
        block = randomized_quicksort(block, 0, len(block)-1)
        idx = bisect.bisect_left(block, x)
        print(block[idx]-block[idx-1])

