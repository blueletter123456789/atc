lst = list(map(int, input().split()))
if lst[1] == sorted(lst)[1]:
    print('Yes')
else:
    print('No')
