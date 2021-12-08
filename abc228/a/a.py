s, t, x = map(int, input().split())
if s <= x < t or (s > t and (x < t or x >= s)):
    print('Yes')
else:
    print('No')
