n, y = map(int, input().split())
a = b = c = -1
k = [10000, 5000, 1000]
if n*k[0] >= y:
    for i in range(n, -1, -1):
        if i*k[0] > y:
            continue
        for j in range(n-i, -1, -1):
            s = n - i - j
            if s >= 0:
                if y == i*k[0] + j*k[1] + s*k[2]:
                    a, b, c = i, j, s
                    break
print(a, b, c)
