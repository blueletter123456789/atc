a, b = input().split()
sum_a, sum_b = 0, 0
for i in a:
    sum_a += int(i)
for i in b:
    sum_b += int(i)
print(max(sum_a, sum_b))
