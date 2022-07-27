h, w, x, y = map(int, input().split())
x -= 1
y -= 1

d = [1, -1]

area = list()
for _ in range(h):
    area.append(input())

ans = 0
for k in range(2):
    for i in range(1, h):
        nx = x + d[k]*i
        if nx < 0 or nx >= h or area[nx][y] == '#':
            break
        ans += 1
    
    for j in range(1, w):
        ny = y + d[k]*j
        if ny < 0 or ny >= w or area[x][ny] == '#':
            break
        ans += 1

print(ans + 1)
