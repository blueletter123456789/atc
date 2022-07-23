from collections import Counter

def solved():
    seen = set()
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    tmp = str(a) + str(b) + str(c) + str(d)
                    flg = True
                    for i, val in enumerate(S):
                        if val == 'x' and str(i) in tmp:
                            flg = False
                            break
                        if val == 'o' and str(i) not in tmp:
                            flg = False
                            break
                    if flg:
                        seen.add(tmp)
    return len(seen)


if __name__ == '__main__':
    S = input()
    pswd = Counter(list(S))

    if pswd['o'] > 4:
        print(0)
    else:
        print(solved())

# Sample code: 全探索
# S = input()
# ans = 0
# for i in range(10000):
#     flag = [False]*10
#     now = i
#     for j in range(4):
#         flag[now%10] = True
#         now //= 10
#     flag2 = True
#     for j in range(10):
#         if S[j] == 'o' and not flag[j]:
#             flag2 = False
#         if S[j] == 'x' and flag[j]:
#             flag2 = False
#     ans += flag2
# print(ans)

# Sample code: 二項定理
# from collections import Counter

# def ncr(a, b, facts):
#     return facts[a]//(facts[b]*facts[a-b])

# def solved():
#     cnt = Counter(list(S))
#     used, unused, unknown = cnt['o'], cnt['x'], cnt['?']

#     if used > 4:
#         return 0
    
#     if used + unknown < 1:
#         return 0
    
#     facts = [0]*10
#     facts[0] = 1
#     for i in range(1, 10):
#         facts[i] = i * facts[i-1]
    
#     res = 0
#     for add in range(unknown+1):
#         num = used + add
#         if num == 0 or num > 4:
#             continue

#         if num == 1:
#             res += ncr(unknown, add, facts)
#         elif num == 2:
#             res += (2*4 + ncr(4, 2, facts)) * ncr(unknown, add, facts)
#         elif num == 3:
#             res += 3*4*3 * ncr(unknown, add, facts)
#         elif num == 4:
#             res += 4*3*2 * ncr(unknown, add, facts)
#     return res



# if __name__ == '__main__':
#     S = input()
#     print(solved())
