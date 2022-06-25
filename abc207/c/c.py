def get_sep(t, l, r):
    delta = 1e-4
    if t == 2:
        r -= delta
    elif t == 3:
        l += delta
    elif t == 4:
        l += delta
        r -= delta
    return l, r

n = int(input())

in_lst = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    ti, li, ri = in_lst[i]
    li, ri = get_sep(ti, li, ri)
    for j in range(i+1, n):
        tj, lj, rj = in_lst[j]
        lj, rj = get_sep(tj, lj, rj)
        if max(li, lj) <= min(ri, rj):
            ans += 1

print(ans)
