n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
max_a = max(1-a, 1-b)
min_a = min(n-a, n-b)
max_b = max(1-a, b-n)
min_b = min(n-a, b-1)
m = []
for k in range(max_a, min_a+1):
    m.append([k+a, k+b])
for k in range(max_b, min_b+1):
    m.append([k+a, b-k])
for i in range(p, q+1):
    l = []
    for j in range(r, s+1):
        if [i,j] in m:
            l.append('#')
        else:
            l.append('.')
    print(''.join(l))
