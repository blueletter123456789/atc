import bisect

h, w, n = map(int, input().split())
x_set = set()
y_set = set()
lst = list()
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
    x_set.add(x)
    y_set.add(y)
x_set = sorted(list(x_set))
y_set = sorted(list(y_set))
for i in range(n):
    x, y = lst[i]
    cnt_x = bisect.bisect_right(x_set, x)
    cnt_y = bisect.bisect_right(y_set, y)
    print(cnt_x, cnt_y)


""" sample source

h, w, n = map(int, input().split())
X, Y = list(), list()
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X_dict = {x: i+1 for i, x in enumerate(sorted(set(X)))}
Y_dict = {y: i+1 for i, y in enumerate(sorted(set(Y)))}
for i in range(n):
    print(X_dict[X[i]], Y_dict[Y[i]])

"""
