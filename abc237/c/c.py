l1 = list(input())
i = len(l1)-1
cnt1 = cnt2 = 0
for j in range(len(l1)):
    if l1[j] == 'a':
        cnt2 += 1
    else:
        break
while i > 0:
    if l1[i] == 'a':
        cnt1 += 1
        i -= 1
    else:
        break
cnt = cnt1-cnt2
if cnt > 0:
    l1 = ['a']*cnt + l1
l2 = l1.copy()
l2.reverse()
res = True
for k in range(len(l1)):
    if l1[k] != l2[k]:
        res = False
        break
if res:
    print('Yes')
else:
    print('No')
