n = int(input())
a = list(map(int, input().split()))
l = [False]*360
l[0] = True
tmp = 0
for i in a:
    r = (tmp+i) % 360
    l[r] = True
    tmp += i
max_r = 0
tmp = 0
for j in range(len(l)):
    if l[j]:
        r = j-tmp
        if max_r < r:
            max_r = r
        tmp = j
print(max(max_r, 360-tmp))
