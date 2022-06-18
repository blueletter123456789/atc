n, k = map(int, input().split())
numbers = list(map(int, input().split()))

idx = {i: v for i, v in enumerate(numbers)}
cnt = {i: False for i in numbers}

numbers.sort()
base = k // n
for i in range(k % n):
    cnt[numbers[i]] = True

for i in range(n):
    j = idx[i]
    if cnt[j]:
        print(base + 1)
    else:
        print(base)
