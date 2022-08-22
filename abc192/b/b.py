s = input()

flg = True
for i, char in enumerate(s):
    if ((i+1)%2 and not char.islower()
      or not (i+1)%2 and not char.isupper()):
        flg = False
        break

if flg:
    print('Yes')
else:
    print('No')
