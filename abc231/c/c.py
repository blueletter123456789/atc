# def search(nums, val, n):
#     left, right = -1, n
#     while right - left > 1:
#         mid = (left + right) // 2
#         if nums[mid] < val:
#             left = mid
#         else:
#             right = mid
#     return n-mid

# n, q = map(int, input().split())
# l = list(map(int, input().split()))
# l.sort()
# for _ in range(q):
#     t = int(input())
#     print(search(l, t, n))

import bisect

n, q = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
for _ in range(q):
    t = int(input())
    i = bisect.bisect_left(l, t)
    print(n-i)
