from collections import defaultdict

def main(n):
    d = defaultdict(int)
    for _ in range(n):
        s = input()
        d[s] += 1
    print(len(d))

if __name__ == '__main__':
    n = int(input())
    main(n)
