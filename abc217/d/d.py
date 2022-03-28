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

class Node(object):
    def __init__(self, val, pivot):
        self.value = val
        self.pivot = pivot
        self.left = None
        self.right = None


class BalancingTree(object):
    def __init__(self, n) -> None:
        self.N = n
        self.root = Node(1<<n, 1<<n)
    
    def append(self, val):
        val += 1
        node = self.root
        while True:
            if val == node.value:
                return 0
            mi, ma = min(val, node.value), max(val, node.value)
            if mi < node.pivot:
                node.value = ma
                if node.left:
                    node = node.left
                    val = mi
                else:
                    p = node.pivot
                    node.left = Node(mi, p-(p&-p)//2)
                    break
            else:
                node.value = mi
                if node.right:
                    node = node.right
                    val = ma
                else:
                    p = node.pivot
                    node.right = Node(ma, p+(p&-p)//2)
                    break
    
    def find_l(self, val):
        val += 1
        node = self.root
        prev = 0
        if node.value < val:
            prev = node.value
        while True:
            if val <= node.value:
                if node.left:
                    node = node.left
                else:
                    return prev - 1
            else:
                prev = node.value
                if node.right:
                    node = node.right
                else:
                    return prev - 1
    
    def find_r(self, val):
        val += 1
        node = self.root
        prev = 0
        if node.value > val:
            prev = node.value
        while True:
            if val < node.value:
                prev = node.value
                if node.left:
                    node = node.left
                else:
                    return prev - 1
            else:
                if node.right:
                    node = node.right
                else:
                    return prev - 1

import math

l, q = map(int, input().split())
l_log2 = int(math.log2(l))+1
bt = BalancingTree(l_log2)
bt.append(0)
bt.append(l)
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        bt.append(x)
    else:
        val_left = bt.find_l(x)
        val_right = bt.find_r(x)
        print(val_right-val_left)
