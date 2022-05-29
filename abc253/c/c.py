import heapq
from collections import defaultdict

q = int(input())

max_lst = list()
min_lst = list()
nums = defaultdict(int)

for i in range(q):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        x = lst[1]
        if x not in nums:
            heapq.heappush(max_lst, -x)
            heapq.heappush(min_lst, x)
        nums[x] += 1
    elif lst[0] == 2:
        x = lst[1]
        c = lst[2]
        if nums[x] <= c:
            del nums[x]
        else:
            nums[x] -= c
    else:
        while True:
            if min_lst[0] in nums:
                break
            heapq.heappop(min_lst)
        while True:
            if (-1*max_lst[0]) in nums:
                break
            heapq.heappop(max_lst)
        print((-1*max_lst[0])-min_lst[0])
