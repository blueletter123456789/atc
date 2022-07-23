from collections import defaultdict

n = int(input())
seen = defaultdict(int)

for _ in range(n):
    s = input()
    if s not in seen:
        print(s)
    else:
        print(s + '({})'.format(seen[s]))
    
    seen[s] += 1
