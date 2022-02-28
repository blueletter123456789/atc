from collections import defaultdict
m, n = map(int, input().split())
A = defaultdict(int)
for i in list(map(int, input().split())):
    A[i] += 1

B = list(map(int, input().split()))
res = True
for i in B:
    a = A.get(i, 0)
    if a <= 0:
        res = False
        break
    A[i] -= 1
if res:
    print('Yes')
else:
    print('No')
