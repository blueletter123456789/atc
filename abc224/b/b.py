def main(h, w, l):
    for i in range(h-1):
        for j in range(i+1, h):
            for n in range(w-1):
                for m in range(n+1, w):
                    if l[i][n] + l[j][m] <= l[i][m] + l[j][n]:
                        continue
                    else:
                        print('No')
                        return
    print('Yes')

if __name__ == '__main__':
    h, w = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(h)]
    main(h, w, l)