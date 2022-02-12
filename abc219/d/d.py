n = int(input())
x, y = map(int, input().split())
max_num = max(x, y)
dpx = [[0]*max_num for _ in range(n+1)]
dpy = [[0]*max_num for _ in range(n+1)]
a, b = map(int, input().split())
dpx[1][a] = 1
dpy[1][b] = 1
for i in range(2, n+1):
    a, b = map(int, input().split())
    max_ab = max(a, b)
    for j in range(0, max_num):
        if(j < max_ab): 
            dpx[i][j] = dpx[i-1][j]
            dpy[i][j] = dpy[i-1][j]
            continue
        if dpx[i-1][j] > dpx[i-1][j-a]+1:
            dpx[i][j] = dpx[i-1][j-a]+1
            dpy[i][j] = dpy[i-1][j-b]+1
        else:
            dpx[i][j] = dpx[i-1][j]
            dpy[i][j] = dpy[i-1][j]
print(dpx)
print(dpy)
