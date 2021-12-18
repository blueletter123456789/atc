from collections import defaultdict
def main(n):
    d = defaultdict(int)
    for _ in range(n-1):
        a, b = map(str, input().split())
        d[a] += 1
        d[b] += 1
    if d[a] == n-1 or d[b] == n-1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    n = int(input())
    main(n)