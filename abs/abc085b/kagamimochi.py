n = int(input())
l = [int(input()) for _ in range(n)]
l.sort(reverse=True)
s = 0
t = 101
for i in l:
    if t > i:
        s += 1
        t = i
print(s)
