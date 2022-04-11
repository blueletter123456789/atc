n = int(input())
s = list()
t = list()
ans = True
for _ in range(n):
    sp, tp = input().split()
    s.append(sp)
    t.append(tp)

for i in range(n):
    flg = [True]*2
    for j in range(n):
        if i == j:
            continue
        if s[i] == s[j] or s[i] == t[j]:
            flg[0] = False
        if t[i] == s[j] or t[i] == t[j]:
            flg[1] = False
    if any(flg):
        continue
    else:
        ans = False
        break

if ans:
    print('Yes')
else:
    print('No')
