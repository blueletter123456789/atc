def win(a, b):
    if a == b:
        return 0
    m = {'G': 'C', 'C': 'P', 'P': 'G'}
    if m[a] == b:
        return 1
    return 2

def main(n, m, l):
    d = [[k, 0] for k in range(n*2)]
    for i in range(m):
        for k in range(0,n):
            res = win(l[d[k*2][0]][i], l[d[k*2+1][0]][i])
            if res == 1:
                d[k*2][1] += 1
            elif res == 2:
                d[k*2+1][1] += 1
        d.sort(key=lambda x: x[0])
        d.sort(reverse=True, key=lambda x: x[1])
    for i in d:
        print(i[0]+1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    l = [list(input()) for _ in range(2*n)]
    main(n, m, l)
