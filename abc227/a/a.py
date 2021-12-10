n, k, a = map(int, input().split())
s = (k+a-1)%n
if s == 0:
    print(n)
else:
    print(s)
