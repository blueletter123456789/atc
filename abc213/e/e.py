# from collections import deque

# d_x = [1, 0, -1, 0]
# d_y = [0, 1, 0, -1]

# INF = 1 << 19

# h, w = map(int, input().split())
# al = list()
# for _ in range(h):
#     al.append(list(input()))
# dist = [[INF]*w for _ in range(h)]
# dist[0][0] = 0
# que = deque([(0, 0)])
# while len(que):
#     x, y = que.popleft()
#     for k in range(4):
#         nx, ny = x+d_x[k], y+d_y[k]
#         if nx < 0 or nx >= h or ny < 0 or ny >= w:
#             continue
#         if al[nx][ny] == '#':
#             if dist[nx][ny] > dist[x][y]+1:
#                 dist[nx][ny] = dist[x][y]+1
#                 que.append((nx, ny))
#         else:
#             if dist[nx][ny] > dist[x][y]:
#                 dist[nx][ny] = dist[x][y]
#                 que.appendleft((nx, ny))
# print((dist[h-1][w-1]+ 2) // 3)

from collections import deque

d_x = [1, 0, -1, 0]
d_y = [0, 1, 0, -1]

INF = 1 << 19

h, w = map(int, input().split())
al = list()
for _ in range(h):
    al.append(list(input()))
dist = [[INF]*w for _ in range(h)]
seen = [[False]*w for _ in range(h)]

dist[0][0] = 0
que = deque([(0, 0)])
while len(que):
    x, y = que.popleft()
    if seen[x][y]:
        continue
    seen[x][y] = True
    for k in range(4):
        nx, ny = x+d_x[k], y+d_y[k]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if al[nx][ny] == '.':
            if dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y]
                que.appendleft((nx, ny))
    for nx in range(x-2, x+3):
        for ny in range(y-2, y+3):
            if abs(x-nx) + abs(y-ny) == 4:
                continue
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))
print(dist[h-1][w-1])
