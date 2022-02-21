from collections import defaultdict

s = list(input())
s_len = len(s)
k = int(input())
X_list = defaultdict(bool)
for i in range(s_len):
    if s[i] == 'X':
        X_list[i] = True
    else:
        X_list[i] = False
ans = 0
for key, val in X_list.items():
    k_cnt = 0
    amt = 0
    i = key
    while i < s_len and (k_cnt < k or X_list[i]):
        if X_list[i]:
            amt += 1
        else:
            amt += 1
            k_cnt += 1
        i += 1
    ans = max(ans, amt)
print(ans)
