from collections import defaultdict

p = int(input())

coins = defaultdict(int)
coins[1] = 100
lst = [0]*(11)
lst[1] = 1

for i in range(2, 11):
    lst[i] = i * lst[i-1]
    coins[lst[i]] = 100

ans = 0
while p > 0:
    for num in reversed(lst):
        if num > p or not coins[num]:
            continue
        ans += 1
        coins[num] -= 1
        p -= num
        break

print(ans)
