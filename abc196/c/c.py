n = int(input())

i = 1
ans = 0
while int(str(i)+str(i)) <= n:
    ans += 1
    i += 1

print(ans)


# Smaple code
# s = input()

# if len(s) == 1:
#     print('0')
# elif len(s) % 2:
#     print('9'*(len(s)//2))
# else:
#     l = s[:len(s)//2]
#     r = s[len(s)//2:]
#     if int(l) <= int(r):
#         print(l)
#     else:
#         print(int(l)-1)
