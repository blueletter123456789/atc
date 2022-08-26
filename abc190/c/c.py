n, m = map(int, input().split())

a = [None]*m
b = [None]*m
for i in range(m):
    a[i], b[i] = map(int, input().split())

k = int(input())
c = [None]*k
d = [None]*k
for i in range(k):
    c[i], d[i] = map(int, input().split())

ans = 0
for i in range(1 << k):
    seen = set()
    for j in range(k):
        if i & (1 << j):
            seen.add(c[j])
        else:
            seen.add(d[j])
    
    cnt = 0
    for i in range(m):
        if a[i] in seen and b[i] in seen:
            cnt += 1
    
    ans = max(ans, cnt)

print(ans)

# Sample code
# import itertools

# N, M = map(int, input().split())
# cond = [tuple(map(int, input().split())) for _ in range(M)]
# K = int(input())
# choice = [tuple(map(int, input().split())) for _ in range(K)]

# ans = 0
# for balls in itertools.product(*choice):
#     balls = set(balls)
#     cnt = sum(A in balls and B in balls for A, B in cond)
#     if ans < cnt:
#         ans = cnt
# print(ans)
