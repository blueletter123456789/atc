n = int(input())
l = list(map(int, input().split()))
ans = [0]*(n+1)
for i in range(1, n+1):
    ans[l[i-1]] = str(i)
ans.pop(0)
print(' '.join(ans))
