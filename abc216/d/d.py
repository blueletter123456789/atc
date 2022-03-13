# from collections import Counter

# n, m = map(int, input().split())
# k = list()
# l = list()
# for i in range(m):
#     k.append(int(input()))
#     l.append(list(map(int, input().split())))

# d = Counter([l[i][0] for i in range(m)])
# s = set()
# for k, v in d.items():
#     if v > 1:
#         s.add(k)
# for i in range(m):
#     if l[i][0] in s:
#         l[i].pop(0)
# while len(s):
#     d = Counter([l[i][0] for i in range(m) if len(l[i])])
#     s = set()
#     for k, v in d.items():
#         if v > 1:
#             s.add(k)
#     for i in range(m):
#         if len(l[i]) and l[i][0] in s:
#             l[i].pop(0)
# if not(all(l)):
#     print('Yes')
# else:
#     print('No')

from collections import deque

n, m = map(int, input().split())
que = deque()
a = [deque() for _ in range(m)]
mem = [list() for _ in range(n)]
for i in range(m):
    k = int(input())
    for j in map(int, input().split()):
        # 各筒の値を格納
        a[i].append(j-1)
    # 各筒の先頭の数字に対してaのインデックスを格納
    mem[a[i][0]].append(i)
for i in range(n):
    if len(mem[i]) == 2:
        # 同時に取り出せるものをキューに格納
        que.append(i)
while len(que):
    current = que.popleft()
    for p in mem[current]:
        # 先頭のものを削除
        a[p].popleft()
        # 次の先頭をキューに格納
        if len(a[p]):
            mem[a[p][0]].append(p)
            if len(mem[a[p][0]]) == 2:
                que.append(a[p][0])
flg = True
for i in a:
    if len(i):
        flg = False
        break
if flg:
    print('Yes')
else:
    print('No')
