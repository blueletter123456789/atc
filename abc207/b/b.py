import math

a, b, c, d = map(int, input().split())

# y = bx+a
# y = cx
# bx + a >= dcx
# bx - cdx >= -a
# x(b-cd) >= -a
# x >= a/(cd-b)
if c*d-b == 0:
    print(-1)
else:
    ans = a / (c*d - b)
    if ans < 0:
        print(-1)
    else:
        print(math.ceil(ans))
