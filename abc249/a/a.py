a, b, c, d, e, f, x = map(int, input().split())
c1 = (x // (a + c))
c2 = (x // (d + f))
t1 = c1*a
t2 = c2*d
if x - (a+c)*c1 > a:
    t1 += a
else:
    t1 += x - (a+c)*c1
if x - (d+f)*c2 > d:
    t2 += d
else:
    t2 += x - (d+f)*c2
ans_t = t1 * b
ans_a = t2 * e
if ans_t == ans_a:
    print('Draw')
elif ans_t > ans_a:
    print('Takahashi')
else:
    print('Aoki')
