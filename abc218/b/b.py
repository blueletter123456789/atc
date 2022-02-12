import string

l = list(map(int, input().split()))
d = dict()
for k, v in enumerate(string.ascii_lowercase):
    d[k+1] = v
ans = ''
for i in l:
    ans += d[i]
print(ans)
