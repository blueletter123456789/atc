dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

h, w = map(int, input().split())

s = list()
for i in range(h):
    s.append(input())

ans = 0
for i in range(h-1):
    for j in range(w-1):
        cnt = 0
        for x, y in zip(dx, dy):
            if s[i+x][j+y] == '#':
                cnt += 1
        
        if cnt == 1 or cnt == 3:
            ans += 1

print(ans)
