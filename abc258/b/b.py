n = int(input())

lst = [list(input()) for _ in range(n)]

dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
ans = 0
for i in range(n):
    for j in range(n):
        for x, y in zip(dx, dy):
            tmp = ''
            for k in range(n):
                xi = (i + k*x) % n
                yj = (j + k*y) % n
                tmp += lst[xi][yj]
            ans = max(ans, int(tmp))

print(ans)
