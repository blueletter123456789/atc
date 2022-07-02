import bisect

n, q = map(int, input().split())
lst = [0] + list(map(int, input().split()))
idxs = [0]*(n+1)
for i in range(1, n+1):
    idxs[i] = idxs[i-1] + (lst[i]-lst[i-1]-1)

for _ in range(q):
    k = int(input())
    idx = bisect.bisect_left(idxs, k)
    if idx > n:
        print(lst[n] + (k - idxs[n]))
    else:
        print(lst[idx-1] + k - idxs[idx-1])
