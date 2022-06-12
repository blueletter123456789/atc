x, a, d, n = map(int, input().split())

max_num = max(a, d*(n-1)+a)
min_num = min(a, d*(n-1)+a)

if min_num < x < max_num:
    tmp = abs((x - a) % d)
    print(min(tmp, abs(d)-tmp))
elif min_num >= x:
    print(abs(min_num-x))
else:
    print(abs(x-max_num))
