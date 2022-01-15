a, b, c = map(int, input().split())
min_num = a//c
max_num = (b//c) + 1
ans = -1
for i in range(min_num, max_num+1):
    tmp = c * i
    if tmp >= a and tmp <= b:
        ans = tmp
        break
print(ans)
