s1 = list(input())
s2 = list(input())
flg = True
if s1[0] != s1[1] and s2[0] != s2[1]:
    if s1[0] == s2[1] and s1[1] == s2[0]:
        flg = False
if flg:
    print('Yes')
else:
    print('No')
