n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]

s_map = list()
t_map = list()
for i in range(n):
    for j in range(n):
        if s[i][j] == '#':
            s_map.append([i, j])
        if t[i][j] == '#':
            t_map.append([i, j])

for _ in range(4):
    res = True
    s_map.sort()
    diff_x = t_map[0][1] - s_map[0][1]
    diff_y = t_map[0][0] - s_map[0][0]
    for k in range(len(s_map)):
        if k >= len(t_map):
            tm = [None, None]
        else:
            tm = t_map[k]
        if (tm[1] != s_map[k][1]+diff_x or 
            tm[0] != s_map[k][0]+diff_y):
            res = False
    for k in range(len(t_map)):
        if k >= len(s_map):
            sm = [None, None]
        else:
            sm = s_map[k]
        if (sm[1] != t_map[k][1]-diff_x or 
            sm[0] != t_map[k][0]-diff_y):
            res = False
    if res:
        break
    for j in range(len(s_map)):
        target = s_map[j]
        s_map[j] = [target[1], (n - 1) - target[0]]
if res:
    print('Yes')
else:
    print('No')
