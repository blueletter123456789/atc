from collections import deque
from collections import defaultdict

n, k = map(int, input().split())
in_lst = list(map(int, input().split()))

que = deque()
que_list = defaultdict(int)
ans = 0
for i in range(n):
    que.append(in_lst[i])
    que_list[in_lst[i]] += 1
    if len(que) > k:
        pop = que.popleft()
        if que_list[pop] == 1:
            del que_list[pop]
        else:
            que_list[pop] -= 1
    ans = max(ans, len(que_list))

print(ans)

""" Sample code
from collections import defaultdict

n, k = map(int, input().split())
in_lst = list(map(int, input().split()))

seen = defaultdict(int)
for i in range(k):
    seen[in_lst[i]] += 1

ans = len(seen)
for i in range(k, n):
    seen[in_lst[i-k]] -= 1
    seen[in_lst[i]] += 1
    if seen[in_lst[i-k]] == 0:
        del seen[in_lst[i-k]]
    ans = max(ans, len(seen))

print(ans)
"""