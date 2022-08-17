def score(S):
    cnt = [0] * 10
    for c in S:
        cnt[int(c)] += 1
    
    ans = 0
    for i in range(1, 10):
        ans += i * (10 ** cnt[i])
    
    return ans

k = int(input())
s = input()
t = input()

# 利用可能なカードの枚数を求める
cnt = [k] * 10

for c in s[:4]:
    cnt[int(c)] -= 1

for c in t[:4]:
    cnt[int(c)] -= 1

ans = 0
# カードの番号が別々の場合
for i in range(1, 10):
    if cnt[i] == 0:
        continue
    for j in range(1, 10):
        if i == j or cnt[j] == 0:
            continue
        if score(s[:4] + str(i)) > score(t[:4] + str(j)):
            ans += cnt[i] * cnt[j]

# カードの番号が同一の場合
for i in range(1, 10):
    if cnt[i] < 2:
        continue
    if score(s[:4] + str(i)) > score(t[:4] + str(i)):
        ans += cnt[i] * (cnt[i] - 1)

# 全てのパターンが(9k-8)C(2)となる
n = k * 9 - 8
print(ans / n / (n-1))

# WA answer
# from collections import Counter

# def calc_score(cnt):
#     ret = 0
#     for i in range(1, 10):
#         num = cnt.get(str(i), 0)
#         ret += i * (10 ** num)
#     return ret

# k = int(input())
# s = input()
# t = input()

# cnt_s = Counter(list(s))
# cnt_t = Counter(list(t))

# win_s = 0
# total = 0
# for i in range(1, 10):
#     for j in range(1, 10):
        
#         i = str(i)
#         j = str(j)

#         if ((cnt_s[i] + cnt_t[i]) == k 
#           or (cnt_s[j] + cnt_t[j]) == k
#           or i == j):
#             continue

#         cnt_s[i] += 1
#         cnt_t[j] += 1
        
#         ss = calc_score(cnt_s)
#         st = calc_score(cnt_t)

#         cnt_s[i] -= 1
#         cnt_t[j] -= 1

#         m = (k - (cnt_s[i] + cnt_t[i])) * (k - (cnt_s[j] + cnt_t[j]))

#         total += m

#         if ss > st:
#             win_s += m

# print(win_s/total)
