from collections import defaultdict
d = defaultdict(int)
n = int(input())
for _ in range(n):
    s = input()
    d[s] += 1
max_d = max(d, key=d.get)
print(max_d)
