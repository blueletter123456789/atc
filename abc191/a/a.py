v, s, t, d = map(int, input().split())

if v*s <= d <= v*t:
    print('No')
else:
    print('Yes')
