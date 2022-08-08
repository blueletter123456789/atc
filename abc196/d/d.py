h, w, a, b = map(int, input().split())

used = [[0]*(w) for _ in range(h)]


def rec(i, j, na, nb, used):
    if j == w:
        return rec(i+1, 0, na, nb, used)
    if i == h:
        return 1
    
    if used[i][j]:
        return rec(i, j+1, na, nb, used)
    
    res = 0
    used[i][j] = 1

    if j+1 < w and not used[i][j+1] and na > 0:
        used[i][j+1] = 1
        res += rec(i, j+1, na-1, nb, used)
        used[i][j+1] = 0
    
    if i+1 < h and not used[i+1][j] and na > 0:
        used[i+1][j] = 1
        res += rec(i, j+1, na-1, nb, used)
        used[i+1][j] = 0
    
    if nb > 0:
        res += rec(i, j+1, na, nb-1, used)
    
    used[i][j] = 0

    return res 

print(rec(0, 0, a, b, used))
