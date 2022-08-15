n = int(input())

min_a, min_b = float('inf'), float('inf')
idx_ma, idx_mb = 0, 0
sec_a, sec_b = float('inf'), float('inf')
idx_sa, idx_sb = 0, 0

for i in range(n):
    a, b = map(int, input().split())
    
    if min_a >= a:
        sec_a, idx_sa = min_a, idx_ma
        min_a, idx_ma = a, i
    elif sec_a >= a:
        sec_a, idx_sa = a, i
    
    if min_b >= b:
        sec_b, idx_sb = min_b, idx_sb
        min_b, idx_mb = b, i
    elif sec_b >= b:
        sec_b, idx_sb = b, i

if idx_ma == idx_mb:
    print(min(max(min_a, sec_b), max(min_b, sec_a), min_a+min_b))
else:
    print(max(min_a, min_b))

# Sample code.
# n = int(input())
# a = [0]*n
# b = [0]*n

# for i in range(n):
#     a[i], b[i] = map(int, input().split())

# res = 10**6
# for i, ai in enumerate(a):
#     for j, bj in enumerate(b):
#         res = min(res, ai+bj if i==j else max(ai, bj))

# print(res)
