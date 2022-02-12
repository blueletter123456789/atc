x = list(input())
n = int(input())
d = {v: k+1 for k, v in enumerate(x)}
l = list()
for _ in range(n):
    s = input()
    res = list()
    for j in s:
        res.append(d[j])
    l.append([res, s])
l.sort(key=lambda x: x[0])
for i in l:
    print(i[1])
