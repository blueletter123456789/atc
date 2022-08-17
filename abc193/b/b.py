n = int(input())

ans = float('inf')
for _ in range(n):
    a, p, x = map(int, input().split())
    if x - a <= 0:
        continue
    ans = min(ans, p)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
