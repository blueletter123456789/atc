# Sample code
n, q, x = map(int, input().split())
w = list(map(int, input().split()))

# 接頭和 (2周分)
acc = [0]
for i in range(2 * n):
    acc.append(acc[-1] + w[i % n])

total = acc[n]  # 総和

# x kg == xr * n個 + xm kg
xm = x %  total
xr = x // total

# iからnext[i]-1まで詰めるとxm kg以上になる
next = [0] * n
i, j = 0, 0
while i < n:
    if acc[j] - acc[i] >= xm:
        next[i] = j
        i += 1
    else:
        j += 1

# seq[k] == k番目の箱の先頭じゃがいも番号
seq = []
visited = set()
i = 0
while i not in visited:
    visited.add(i)
    seq.append(i)
    i = next[i] % n

# seq[cyclehead] -> ... -> seq[-1] -> seq[cyclehead] -> ...
cyclehead = [k for k, s in enumerate(seq) if s == next[seq[-1]] % n][0]

# potato[k] == k番目の箱のじゃがいも数
potato = [next[s] - s + xr * n for s in seq]

for _ in range(q):
    k = int(input())
    k -= 1
    if k >= cyclehead:
        k -= cyclehead
        k %= len(potato) - cyclehead
        k += cyclehead
    print(potato[k])

    
        

# import bisect

# n, q, x = map(int, input().split())
# W  = list(map(int, input().split()))
# sum_w = [0]*n
# sum_w[0] = W[0]
# for i in range(1, n):
#     sum_w[i] = sum_w[i-1] + W[i]

# print(sum_w)
# for _ in range(q):
#     k = int(input())
#     k *= x
#     idx = bisect.bisect(sum_w, k % sum_w[-1])
#     print(k, idx)
