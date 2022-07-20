s = input()
d = {'6': '9', '9': '6'}

ans = ''
for i in reversed(s):
    ans += d.get(i, i)
print(ans)
