n, x = map(int, input().split())
lst = list(map(int, input().split()))

sum_num = 0
for i in range(n):
    if (i + 1) % 2 == 0:
        sum_num += (lst[i] - 1)
    else:
        sum_num += lst[i]

if sum_num <= x:
    print('Yes')
else:
    print('No')

# Another code
# n, x = map(int, input().split())
# lst = list(map(int, input().split()))
# if sum(lst) - n//2 <= x:
#     print('Yes')
# else:
#     print('No')
