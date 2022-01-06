def main(n, p, l):
    cnt = 0
    for i in range(n):
        if p > l[i]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    n, p = map(int, input().split())
    l = list(map(int, input().split()))
    main(n, p, l)
