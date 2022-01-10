def main(n, k, l):
    t = sorted(l[:k], reverse=True)
    for i in range(k, n+1):
        # t = sorted(l[:i], reverse=True)
        if k != i:
            flg = True
            for j in range(len(t)):
                if t[j] < l[i-1]:
                    t.insert(j, l[i-1])
                    flg = False
                    break
            if flg:
                t.append(l[i-1])
        print(t[k-1])

if __name__ == '__main__':
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    main(n, k, l)
