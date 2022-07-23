n = int(input())
M = list()
for _ in range(n):
    s, t = input().split()
    M.append((int(t), s))
M.sort()
print(M[-2][1])
