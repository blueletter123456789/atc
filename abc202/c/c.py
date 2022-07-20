from collections import Counter

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

a_lst = Counter(A)
ans = 0
for i in range(n):
    if B[C[i]-1] in a_lst:
        ans += a_lst[B[C[i]-1]]

print(ans)
