n = int(input())

score = [input() for _ in range(n)]

ans = True
for i in range(n):
    for j in range(i+1, n):
        if score[i][j] == 'D' and score[j][i] != 'D':
            ans = False
            break
        elif score[i][j] == 'W' and score[j][i] != 'L':
            ans = False
            break
        elif score[i][j] == 'L' and score[j][i] != 'W':
            ans = False
            break

if ans:
    print('correct')
else:
    print('incorrect')
