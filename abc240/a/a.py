a, b = map(int, input().split())
b %= 10
ans1 = (a-1)%10
ans2 = (a+1)%10
if ans1 == b or ans2 == b:
    print('Yes')
else:
    print('No')
