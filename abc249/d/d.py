def prime_calc(tgt):
    lim = int(tgt**0.5)+1
    res = set()
    for i in range(1, lim+1):
        if tgt % i != 0:
            continue
        res.add((i, tgt//i))
        if i != tgt//i:
            res.add((tgt//i, i))
    return res

from collections import Counter
n = int(input())
lst = list(map(int, input().split()))
cnt = Counter(lst)

nums = list()
ans = 0
for i in range(n):
    nums = prime_calc(lst[i])
    for k1, k2 in nums:
        ans += cnt[k1] * cnt[k2]
print(ans)
