n = int(input())
A = list(map(int, input().split()))

ans = float('inf')
for i in range(1 << (n-1)):
    num_or = A[0]
    num_xor = 0
    # print(bin(i))
    for j in range(1, n):
        if i & (1 << (j-1)):
            num_xor ^= num_or
            num_or = 0
        num_or |= A[j]
    num_xor ^= num_or
    ans = min(ans, num_xor)

print(ans)
