def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n, a, b = map(int, input().split())
if a == b:
    cnt_a = n // a
    ans_a = (cnt_a*(cnt_a+1)//2)*a
    print(n*(n+1)//2 - ans_a)
else:
    cnt_a = n//a
    cnt_b = n//b
    ab = a*b//gcd(a, b)
    cnt_ab = n//(ab)
    ans_a = (cnt_a*(cnt_a+1)//2)*a
    ans_b = (cnt_b*(cnt_b+1)//2)*b
    ans_ab = (cnt_ab*(cnt_ab+1)//2)*(ab)
    minus = ans_a + ans_b - ans_ab
    print(n*(n+1)//2 - minus)
