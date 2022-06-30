from collections import defaultdict

n = int(input())
in_lst = list(map(int, input().split()))
seen = defaultdict(int)
cnt = 0
for i, num in enumerate(reversed(in_lst)):
    if num in seen:
        cnt += i-seen[num]
    else:
        cnt += i
    seen[num] += 1

print(cnt)

# import bisect

# n = int(input())
# in_lst = list(map(int, input().split()))
# lst = []
# cnt = 0
# for num in reversed(in_lst):
#     idx = bisect.bisect(lst, num)
#     cnt += len(lst)-idx
#     lst = lst[:idx] + [num] + lst[idx:]
# print(cnt)
