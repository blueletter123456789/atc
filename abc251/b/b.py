n, w = map(int, input().split())
in_lst = list(map(int, input().split()))

in_set = [False]*(w+1)
ans = 0
for i in range(n):
    if in_lst[i] <= w:
        in_set[in_lst[i]] = True
    for j in range(i+1, n):
        if in_lst[i] + in_lst[j] <= w:
            in_set[in_lst[i] + in_lst[j]] = True
        for k in range(j+1, n):
            if in_lst[i] + in_lst[j] + in_lst[k] <= w:
                in_set[in_lst[i] + in_lst[j] + in_lst[k]] = True
ans = 0
for b in in_set:
    if b:
        ans += 1
print(ans)
