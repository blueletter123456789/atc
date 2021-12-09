from collections import defaultdict
n, x = map(int, input().split())
l = input().split()
t = defaultdict(int)
for _ in range(n):
    t[str(x)] += 1
    if t[str(x)] > 1:
        break
    x = int(l[x-1])
print(len(t))