n = int(input())
score = list()
idx_set = set()
for i in range(n):
    s, t = input().split()
    if s in idx_set:
        continue
    score.append((int(t), i+1))
    idx_set.add(s)

score.sort(reverse=True, key=lambda x: x[0])
ans, tgt = score[0][0], score[0][1]
for point, idx in score:
    if ans > point:
        break
    if tgt > idx:
        tgt = idx
print(tgt)
