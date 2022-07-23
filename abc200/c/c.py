from collections import defaultdict
import bisect


n = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(list)
for i, a in enumerate(A):
    cnt[a%200].append(i)

ans = 0
for i, a in enumerate(A):
    tgt = (a + 200) % 200
    if tgt not in cnt:
        continue
    idx = bisect.bisect(cnt[tgt], i)
    ans += len(cnt[tgt]) - idx

print(ans)

# Sample code
# n = int(input())
# A = list(map(int, input().split()))

# b = defaultdict(int)
# for i in A:
#     b[i%200] += 1

# res = 0
# for k in range(200):
#     if k in b:
#         res += (b[k]*(b[k]-1)) // 2

# print(res)
