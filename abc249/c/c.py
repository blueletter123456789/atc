from collections import Counter
n, k = map(int, input().split())
lst = [input() for _ in range(n)]
ans = 0

for i in range(1 << n):
    tmp = list()
    for j in range(n):
        if i & 1 << j:
            tmp += list(lst[j])
    cnt = Counter(tmp)
    res = 0
    for key, val in cnt.items():
        if val == k:
            res += 1
    ans = max(ans, res)
print(ans)
