n = int(input())

seen = set()
i = 2
while i*i <= n:
    j = 2
    while i**j <= n:
        seen.add(i**j)
        j += 1
    i += 1

print(n - len(seen))
