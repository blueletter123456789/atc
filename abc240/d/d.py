# n = int(input())
# l = list(map(int, input().split()))
# ans = list()
# for i in range(n):
#     ans.append(l[i])
#     cnt = 0
#     len_ans = len(ans)-1
#     j = len_ans
#     while j >= 0 and ans[len_ans] == ans[j]:
#         cnt += 1
#         j -= 1
#         if cnt == ans[len_ans]:
#             cnt = min(cnt, l[i])
#             ans = ans[:-cnt]
#             len_ans = len(ans)-1
#             j = len_ans
#             cnt = 0
#     print(len(ans))

from collections import deque

n = int(input())
l = list(map(int, input().split()))
Q = deque([l[0]])
print(1)
for i in range(1, n):
    Q.append(l[i])
    j = len(Q)-1
    cnt = 0
    tmpQ = Q.copy()
    while len(Q) > 0 and Q[j] == Q[-1]:
        cnt += 1
        j -= 1
        tmpQ.pop()
        if cnt == Q[-1]:
            Q = tmpQ.copy()
            j = len(Q)-1
            cnt = 0
    print(len(Q))
