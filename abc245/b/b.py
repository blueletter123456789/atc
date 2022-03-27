n = int(input())
times = set(map(int, input().split()))
for i in range(2001):
    if i not in times:
        print(i)
        break
