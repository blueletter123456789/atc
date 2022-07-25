n = input()
n = n.rstrip('0')

j = len(n)-1
ans = True
for i in range(len(n)//2):
    if n[i] != n[j]:
        ans = False
        break
    j -= 1

if ans:
    print('Yes')
else:
    print('No')


# Smaple code
# n = input()
# n = n.rstrip('0')

# if n == n[::-1]:
#     print('Yes')
# else:
#     print('No')
