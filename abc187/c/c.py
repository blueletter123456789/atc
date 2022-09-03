n = int(input())

seen = set()
s = list()
for i in range(n):
    si = input()
    if si[0] == '!':
        seen.add(si[1:])
    else:
        s.append(si)

flg = ''
for char in s:
    if char in seen:
        flg = char
        break

if not flg:
    print('satisfiable')
else:
    print(flg)
