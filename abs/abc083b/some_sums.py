n, a, b = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    s = 0
    j = i
    for _ in range(len(str(i))):
        s += j % 10
        j //= 10
    if a <= s <= b:
        cnt += i
print(cnt)
