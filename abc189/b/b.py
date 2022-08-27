from decimal import Decimal

n, x = map(int, input().split())

ans = -1
total = 0
for i in range(n):
    v, p = map(Decimal, input().split())
    total += v*(p/100)
    if total > x:
        ans = i+1
        break

print(ans)

# Sample code.
# N,X = map(int,input().split())
# s = 0

# for i in range(N):
#   v,p = map(int,input().split())
#   s += v*p
#   if s > X*100:
#     print(i+1)
#     exit()

# print(-1)
