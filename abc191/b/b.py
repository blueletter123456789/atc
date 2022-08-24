n, x = input().split()

ans = list()
for num in list(input().split()):
    if x == num:
        continue
    ans.append(num)

print(' '.join(ans))
