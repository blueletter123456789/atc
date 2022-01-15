from collections import defaultdict

n, q = map(int, input().split())
l = list(map(int, input().split()))
d = defaultdict(list)
for i in range(n):
    d[l[i]].append(i)

for _ in range(q):
    k, v = map(int, input().split())
    if len(d[k]) < v:
        print(-1)
    else:
        print(d[k][v-1]+1)
