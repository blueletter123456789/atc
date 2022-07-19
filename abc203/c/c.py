n, k = map(int, input().split())
lst = list()

for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort()

prev = 0
for i in range(n):
    a, b = lst[i]
    if k < (a-prev):
        break
    k -= (a-prev)
    prev = a
    k += b

print(prev + k)
