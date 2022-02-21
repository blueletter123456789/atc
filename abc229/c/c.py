n, w = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort(reverse=True)
ans = 0
i = 0
while w > 0 and i < n:
    if w < l[i][1]:
        ans += l[i][0] * w
    else:
        ans += l[i][0] * l[i][1]
    w -= l[i][1]
    i += 1
print(ans)
