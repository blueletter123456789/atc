INF = 10**12

def dp(x, y):
    if vis[y][x]:
        return memo[y][x]
    
    vis[y][x] = True

    turn = (x + y) % 2

    if x == w-1 and y == h-1:
        memo[y][x] = 0
        return 0

    if y < h-1:
        score_y = 1 if G[y+1][x] == '+' else -1
    if x < w-1:
        score_x = 1 if G[y][x+1] == '+' else -1

    if turn == 0:
        memo[y][x] = -INF
        if y < h-1:
            memo[y][x] = max(memo[y][x], dp(x, y+1)+score_y)
        if x < w-1:
            memo[y][x] = max(memo[y][x], dp(x+1, y)+score_x)
        return memo[y][x]
    else:
        memo[y][x] = INF
        if y < h-1:
            memo[y][x] = min(memo[y][x], dp(x, y+1)-score_y)
        if x < w-1:
            memo[y][x] = min(memo[y][x], dp(x+1, y)-score_x)
        return memo[y][x]


if __name__ == '__main__':
    h, w = map(int, input().split())
    G = [input() for _ in range(h)]

    vis = [[False]*w for _ in range(h)]
    memo = [[0]*w for _ in range(h)]

    opt = dp(0, 0)

    if opt > 0:
        print('Takahashi')
    elif opt == 0:
        print('Draw')
    else:
        print('Aoki')
