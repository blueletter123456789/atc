# n = list(input())
# max_num = 0
# n = sorted(n, reverse=True)
# for i in range(1, len(n)):
#     a = []
#     b = []
#     for j in range(1, i+1, 2):
#         a.append(n[j-1])
#         b.append(n[j])
#     b += n[j+1:]
#         # a = n[:i]
#         # b = n[i:]
#         # a = int(''.join(sorted(a, reverse=True)))
#         # b = int(''.join(sorted(b, reverse=True)))
#     a = int(''.join(a))
#     b = int(''.join(b))
#     if max_num < a*b:
#         max_num = a*b
# print(max_num)

N = sorted(input(),reverse=True)
ans = 0
for i in range(1<<len(N)):
    l = 0
    r = 0
    for j in range(len(N)):
        if i & (1<<j):
            l = l*10+ord(N[j])-ord('0')
        else:
            r = r*10+ord(N[j])-ord('0')
    ans = max(ans,l*r)
print(ans)
