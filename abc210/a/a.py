n, a, x, y = map(int, input().split())

ans = 0
for i in range(n):
    if i < a:
        ans += x
    else:
        ans += y

print(ans)

""" Sample code
n, a, x, y = map(int, input().split())

ans = 0
if n > a:
    ans = x*a + y*(n-a)
else:
    ans = x*n

print(ans)
"""