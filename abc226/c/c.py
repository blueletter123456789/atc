def dfs(j, se, l):
    se[j] = True
    for i in l[j]:
        if not i or se[i]:
            continue
        else:
            dfs(i, se, l)

def main(n):
    l = {}
    a = []
    se = {}

    for i in range(n):
        t = []
        t = list(map(int, input().split()))
        a.append(t[0])
        l[i+1] = t[2:]
        se[i+1] = False
    dfs(n, se, l)
    ti = 0
    for k, v in se.items():
        if v: ti += a[k-1]
    print(ti)

if __name__ == '__main__':
    n = int(input())
    main(n)