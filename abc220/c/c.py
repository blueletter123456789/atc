import bisect

n = int(input())
l = list(map(int, input().split()))
x = int(input())
for i in range(1, n):
    l[i] += l[i-1]
sum_idx = (x // l[n-1])*n
x_rem = x % l[n-1]
rem_idx = bisect.bisect_right(l, x_rem)
print(sum_idx+rem_idx+1)
