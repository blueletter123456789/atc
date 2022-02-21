a, b = map(int, input().split())
ans = True
while a > 0 and b > 0:
    num = (a % 10) + (b % 10)
    if num >= 10:
        ans = False
        break
    a //= 10
    b //= 10

if ans:
    print('Easy')
else:
    print('Hard')
