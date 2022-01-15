import bisect

def get_list(n, a):
    l = [1]
    max_num = 1
    while max_num < n:
        max_num *= a
        l.append(max_num)
    l.pop(-1)
    return l

def replace(x):
    if len(str(x)) > 1 and x%10 != 0:
        t = int(str(x)[1:]+str(x)[1])
        return t

def main():
    a, n = map(int, input().split())
    if len(str(n)) == 1 and n%a != 0:
        return -1
    i = 0
    l = get_list(n, a)
    cnt = 0
    while n > a:
        i += 1
        if cnt > len(str(n)):
            return -1
        if n%a != 0:
            n = replace(n)
            cnt += 1
            continue
        cnt = 0
        if n in l:
            t = l.index(n)
            i += t+1
            break
        else:
            n //= a
    return i

if __name__ == '__main__':
    print(main())
