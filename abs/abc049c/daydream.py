s = input()
ans = 'NO'
if len(s) > 4:
    ans = 'YES'
    while len(s) > 0:
        if s.endswith('dream'):
            s = s[:-5]
        elif s.endswith('dreamer'):
            s = s[:-7]
        elif s.endswith('erase'):
            s = s[:-5]
        elif s.endswith('eraser'):
            s = s[:-6]
        else:
            ans = 'NO'
            break
print(ans)