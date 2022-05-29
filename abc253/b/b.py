h, w = map(int, input().split())
lst = list()
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == 'o':
            lst.append((i, j))

print(abs(lst[0][0]-lst[1][0]) + abs(lst[0][1]-lst[1][1]))
