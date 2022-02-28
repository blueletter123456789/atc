n = int(input())
s = [list(input()) for _ in range(n)]
flg = False
for k in range(n**2):
    i, j = k // n, k % n
    cnt = point = 0
    while i < n and j < n:
        if cnt == 6 or (s[i][j] != '#' and point >= 2):
            break
        if s[i][j] != '#':
            point += 1
        cnt += 1
        i += 1
    if cnt == 6:
        flg = True
        break
    i, j = k // n, k % n
    cnt = point = 0
    while i < n and j < n:
        if cnt == 6 or (s[i][j] != '#' and point >= 2):
            break
        if s[i][j] != '#':
            point += 1
        cnt += 1
        j += 1
    if cnt == 6:
        flg = True
        break
    i, j = k // n, k % n
    cnt = point = 0
    while i < n and j < n:
        if cnt == 6 or (s[i][j] != '#' and point >= 2):
            break
        if s[i][j] != '#':
            point += 1
        cnt += 1
        i += 1
        j += 1
    if cnt == 6:
        flg = True
        break
    i, j = k // n, k % n
    cnt = point = 0
    while i < n and j >= 0:
        if cnt == 6 or (s[i][j] != '#' and point >= 2):
            break
        if s[i][j] != '#':
            point += 1
        cnt += 1
        i += 1
        j -= 1
    if cnt == 6:
        flg = True
        break
if flg:
    print('Yes')
else:
    print('No')

