n = int(input())
ans = 'Yes'
s = d = a = b = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    t2 = t - s
    d = abs(x - a) + abs(y - b)
    if (t2%2) != (d%2) or t2 < d:
        ans = 'No'
        break
    a, b, s = x, y, t
print(ans)
