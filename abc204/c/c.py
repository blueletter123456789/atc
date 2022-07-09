import sys
sys.setrecursionlimit(10000)

seen = list()

def dfs(cur):
    global seen
    seen[cur] = True
    cnt = 1
    for v in G[cur]:
        if seen[v]:
            continue
        cnt += dfs(v)
    return cnt


def solved():
    global seen
    ans = 0
    for i in range(n):
        seen = [False]*n
        ans += dfs(i)
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    G = [list() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
    
    print(solved())
