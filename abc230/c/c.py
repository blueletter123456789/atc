n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
ans = [['.' for _ in range(r, s+1)] for _ in range(p, q+1)]
max_a = max(p-a, r-b)
min_a = min(q-a, s-b)
for i in range(max_a, min_a+1):
    ans[a+i-p][b+i-r] = '#'
max_b = max(p-a, b-s)
min_b = min(q-a, b-r)
for i in range(max_b, min_b+1):
    ans[a+i-p][b-i-r] = '#'
for i in range(len(ans)):
    s = ''.join(ans[i])
    print(''.join(ans[i]))
