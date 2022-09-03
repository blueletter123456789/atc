n = int(input())
sum_of_a = 0
sum_of_t = []
for i in range(n):
    A, B = map(int, input().split())
    # increase my A+B, decrease another A
    sum_of_a -= A
    sum_of_t.append(A + A + B)
sum_of_t.sort()
ans = 0
# if x > 0, it means sum of my A+B > another sum of A
while sum_of_a <= 0:
    sum_of_a += sum_of_t.pop()
    ans += 1
print(ans)

# search all
# n = int(input())
# a = list()
# b = list()
# for _ in range(n):
#     i, j = map(int, input().split())
#     a.append(i)
#     b.append(j)

# ans = float('inf')
# for i in range(1 << n):
#     cnt_t = 0
#     cnt_a = 0
#     cnt = 0
#     for j in range(n):
#         if i & (1 << j):
#             cnt_t += a[j] + b[j]
#             cnt += 1
#         else:
#             cnt_a += a[j]
#     if cnt_t > cnt_a:
#         ans = min(ans, cnt)

# print(ans)
