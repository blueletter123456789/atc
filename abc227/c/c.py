import math

def main(n):
    cnt = 0
    for a in range(1, math.ceil(math.pow(n, 1/3))+1):
        for b in range(a, math.ceil(math.pow(n/a, 1/2))+1):
            c = int(n / (a*b))
            if a <= b <= c:
                cnt += c+1-b
            else:
                break
    print(cnt)

if __name__ == '__main__':
    n = int(input())
    main(n)
