import string

s = input()
chars = set()
flg = [False, False, True]
for i in s:
    if i in string.ascii_uppercase:
        flg[0] = True
    if i in string.ascii_lowercase:
        flg[1] = True
    if i in chars:
        flg[2] = False
    chars.add(i)
if all(flg):
    print('Yes')
else:
    print('No')
