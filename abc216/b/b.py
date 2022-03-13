n = int(input())
l = [input().split() for _ in range(n)]
flg = False
for i in range(n):
    for j in range(i+1, n):
        if l[i][0] == l[j][0] and l[i][1] == l[j][1]:
            flg = True
            break
if flg:
    print('Yes')
else:
    print('No')
