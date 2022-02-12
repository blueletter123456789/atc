n = 3
l = ['']*n
for i in range(n):
    l[i] = input()
t = list(input())
ans = ''
for i in t:
    idx = int(i)-1
    ans += l[idx]
print(ans)
