n = int(input())
r = 2
for i in range(65):
    if r**i > n:
        print(i-1)
        break
