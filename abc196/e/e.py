N = int(input())
low = -1 << 60
high = 1 << 60
add = 0
for i in range(N):
    A, T = map(int, input().split())
    if T == 1:
        low += A
        high += A
        add += A
    elif T == 2:
        if low < A:
            low = A
        if high < A:
            high = A
    else:
        if low > A:
            low = A
        if high > A:
            high = A
input()
for x in map(int, input().split()):
    print(min(high, max(low, x + add)))


# TLE source code.
# from collections import defaultdict
# import sys

# sys.setrecursionlimit(10**6)

# def func1(i, x):
#     return x + A[i]

# def func2(i, x):
#     return max(x, A[i])

# def func3(i, x):
#     return min(x, A[i])

# def calc(i, x):
#     if i < 0:
#         return x
    
#     if x in seen[T[i]]:
#         return seen[T[i]][x]
    
#     res = 0
#     if T[i] == 1:
#         res = func1(i, calc(i-1, x))
#         seen[T[i]][x] = res
#     elif T[i] == 2:
#         res = func2(i, calc(i-1, x))
#         seen[T[i]][x] = res
#     else:
#         res = func3(i, calc(i-1, x))
#         seen[T[i]][x] = res
    
#     return res

# n = int(input())
# A = [0]*n
# T = [0]*n
# for i in range(n):
#     A[i], T[i] = map(int, input().split())
# q = int(input())
# X = [int(i) for i in input().split()]
# seen = [defaultdict(int) for _ in range(4)]

# for i in range(q):
#     x = X[i]
#     print(calc(n-1, x))
