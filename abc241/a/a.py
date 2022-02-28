l = list(map(int, input().split()))
ans = l[0]
for _ in range(2):
    ans = l[ans]
print(ans)
