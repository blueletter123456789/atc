from collections import Counter

n = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

ans = 0
for k1, val1 in cnt.items():
    for k2, val2 in cnt.items():
        if k1 > k2:
            continue

        if k1 == k2:
            continue

        ans += (k2-k1)*(k2-k1)*val1*val2

print(ans)

# n = int(input())
# A = list(map(int, input().split()))

# num_a = num_b = 0
# for i, a in enumerate(A):
#     num_a += i*a
#     num_b += (n-i)*a

# print(num_a, num_b)
# print((num_a-num_b)**2)
