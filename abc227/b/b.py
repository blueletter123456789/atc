def is_ng(s):
    for i in range(1, s):
        t = s - 3*i
        if t > 0:
            for j in range(1, t):
                if s == 4*i*j + 3*(i+j):
                    return False
    return True

def main(n, l):
    cnt = 0
    for s in l:
        if is_ng(s):
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    main(n, l)
