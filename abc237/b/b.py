h, w = map(int, input().split())
l = [input().split() for _ in range(h)]
for i in range(w):
    res = list()
    for j in range(h): 
        res.append(l[j][i])
    print(' '.join(res))
