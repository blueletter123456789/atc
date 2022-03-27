""" wrong answer
n, m = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = [0]*(m+1)
for i in range(m+n):
    for j in range(n+1):
        print(f'{i=}, {j=}')
        idx = m-j
        ans[idx] += C[i] // A[j]
print(ans)
"""

n, m = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = [0]*(m+1)
for i in range(m, -1, -1):
    B[i] = C[n+i]//A[n]
    for j in range(n+1):
        C[i+j] -= A[j]*B[i]
print(' '.join([str(i) for i in B]))
