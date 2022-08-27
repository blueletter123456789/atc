n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for x, y in zip(a, b):
    ans += x*y

if ans == 0:
    print('Yes')
else:
    print('No')
