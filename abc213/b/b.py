n = int(input())
lst = list(map(int, input().split()))
max_val = max_idx = 0
bub_val = bub_idx = 0
for i in range(n):
    if max_val < lst[i]:
        bub_val = max_val
        max_val = lst[i]
        bub_idx = max_idx
        max_idx = i + 1
    elif bub_val < lst[i]:
        bub_val = lst[i]
        bub_idx = i + 1
print(bub_idx)
