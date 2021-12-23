def main(n):
    t = 0
    l = []
    for i in range(n):
        a, b = map(int, input().split())
        t += a/b
        l.append((a, b))
    t /= 2
    w = 0
    for i in range(n):
        t -= l[i][0]/l[i][1]
        if t > 0:
            w += l[i][0]
        else:
            if t == 0:
                w += l[i][0]
            else:
                w += l[i][0] + l[i][1]*t
            print(w)
            break

if __name__ == '__main__':
    n = int(input())
    main(n)
