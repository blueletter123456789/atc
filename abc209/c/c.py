M = 10**9 + 7

n = int(input())
c_lst = list(map(int, input().split()))
c_lst.sort()

cnt = 0
ans = 1
for i in range(n):
    ans *= (c_lst[i]-i) % M
    ans %= M

print(ans)
