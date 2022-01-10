def main(n, l):
    diff = 0
    for i in range(n):
        for j in range(i+1, n):
            s = 0
            s = ((l[i][0]-l[j][0])**2 + (l[i][1]-l[j][1])**2)**0.5
            if s > diff:
                diff = s
    print(diff)

if __name__ == '__main__':
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    main(n, l)
