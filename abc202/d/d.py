def ncr(n, r):
    res = 1
    for i in range(1, r+1):
        res *= n-i+1
        res //= i
    return res


if __name__ == '__main__':
    a, b, k = map(int, input().split())
    k -= 1
    n = a + b
    ans = ''

    for i in range(n):
        if a > 0:
            if k < ncr(a+b-1, b):
                ans += 'a'
                a -= 1
            else:
                ans += 'b'
                k -= ncr(a+b-1, b)
                b -= 1
        else:
            ans += 'b'
            b -= 1

    print(ans)


# TLE source code
# a, b, k = map(int, input().split())

# comb = (1 << b) - 1
# for _ in range(k-1):
    # print(bin(comb))
#     x = comb & -comb
#     y = comb + x
#     comb = ((comb & ~y) // x >> 1) | y
# print(bin(comb))

