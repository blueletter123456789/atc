a, b, c = map(int, input().split())

# a + c > bで判定可能
if c == 0:
    if a > b:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if b > a:
        print('Aoki')
    else:
        print('Takahashi')
