M = 1000000007

def power(a, r):
    p = a
    res = 1
    for i in range(30):
        if r & (1 << i):
            res *= p
            res %= M
        p *= p
        p %= M
    return res

def ncr(a, b, fact):
    if a < 0 or b < 0:
        return 0
    return (fact[a+b] * power((fact[a]*fact[b])%M, M-2))%M

def solved(n, m, k):
    if n > m + k:
        return 0

    fact = [0]*(n+m+1)
    fact[0] = 1
    for i in range(1, n+m+1):
        fact[i] = fact[i-1]*i
        fact[i] %= M

    total = ncr(n, m, fact)
    out = ncr(n-k-1, m+k+1, fact)
    return (total - out) % M

if __name__ == '__main__':
    n, m, k = map(int, input().split())

    print(solved(n, m, k))


# n, m, k = map(int, input().split())

# M = 1000000007

# def power(x, r):
#     p = x
#     ans = 1
#     for i in range(1, 30):
#         if r & (1 << i):
#             ans *= p
#             ans %= M
#         p *= p
#         p %= M
#     return ans

# def ncr(x, r):
#     return (pows[x] * power((pows[r]*pows[x-r]) % M, M-2)) % M

# pows = [0]*(n+m+1)
# pows[1] = 1
# for i in range(2, n+m+1):
#     pows[i] = pows[i-1]*i

# ans = 0
# for i in range(n+1):
#     x = i+k
#     if x > m:
#         continue
#     ans += ncr(i+x, i)
#     ans %= M

# print(ans)
