def main(n, k):
    l = [sum(map(int, input().split())) for _ in range(n)]
    r = sorted(l, reverse=True)
    for i in range(n):
        if l[i]+300 >= r[k-1]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    n, k = map(int, input().split())
    main(n, k)
