def same(s, t):
    if s == t:
        return True
    res1 = ''
    res2 = ''
    a = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            res1 += s[i]
            res2 = t[i] + res2
            a = abs(a)-i
    if len(res1) == 2 and res1 == res2 and a == -1:
        return True
    else:
        return False

if __name__ == '__main__':
    s = input()
    t = input()
    if same(s, t):
        print('Yes')
    else:
        print('No')
