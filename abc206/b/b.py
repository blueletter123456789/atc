n = int(input())

amount = 0
for i in range(1, 10**5):
    amount += i
    if amount >= n:
        break

print(i)
