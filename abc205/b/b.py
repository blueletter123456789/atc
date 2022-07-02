n = int(input())
lst = set(list(map(int, input().split())))

if n == len(lst):
    print('Yes')
else:
    print('No')
