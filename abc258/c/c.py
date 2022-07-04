n, q = map(int, input().split())
s = list(input())
idx = 0

for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        idx -= x
        idx %= n
    elif t == 2:
        tmp = (idx + x - 1) % n
        print(s[tmp])
