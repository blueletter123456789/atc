from collections import deque

q = int(input())
rows = 0
que = deque([])
for _ in range(q):
    tmp = list(map(int, input().split()))
    if len(tmp) == 3:
        que.append((tmp[1], tmp[2]))
    else:
        rows += 1
        num = 0
        ans = 0
        while True:
            x, c = que.popleft()
            if num+c == tmp[1]:
                ans += x*c
                break
            elif num+c < tmp[1]:
                ans += x*c
                num += c
            else:
                cnt = c+num-tmp[1]
                ans += (c-cnt)*x
                que.appendleft((x, cnt))
                break
        print(ans)
if not rows:
    print('')
