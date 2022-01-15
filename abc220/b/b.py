k = int(input())
a, b = map(str, input().split())
ta = tb = 0
for i in range(1, len(a)+1):
    ta += k**(i-1) * int(a[-i])
for i in range(1, len(b)+1):
    tb += k**(i-1) * int(b[-i])
print(ta * tb)
