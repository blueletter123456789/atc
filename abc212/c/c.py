import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

min_num = 1 << 34
for tgt in a:
    idx = bisect.bisect(b, tgt)
    min_num = min(min_num, abs(tgt-b[idx-1]))
    if idx < len(b):
        min_num = min(min_num, abs(tgt-b[idx]))

print(min_num)

# Another source cord
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.sort()
# b.sort()

# ai, bi = 0, 0
# min_diff = 1 << 34
# while ai < n and bi < m:
#     diff = abs(a[ai]-b[bi])
#     min_diff = min(min_diff, diff)
#     if a[ai] < b[bi]:
#         ai += 1
#     elif a[ai] > b[bi]:
#         bi += 1
#     else:
#         min_diff = 0
#         break

# print(min_diff)
