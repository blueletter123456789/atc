n = int(input())

x = list()
y = list()
for _ in range(n):
    i, j = map(int, input().split())
    x.append(i)
    y.append(j)

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = x[i], y[i]
        x2, y2 = x[j], y[j]
        a = abs(y2-y1)/abs(x2-x1)
        # y2-y1 <= x2-x1でも成り立つ
        if a <= 1:
            cnt += 1

print(cnt)
