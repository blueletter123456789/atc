# 初項がa,項数がnであるような等差数列の総和がNとする
# 1/2n(2a+n−1)となり、2N=n(2a+n−1)とできる
# nは2Nの約数となるため、成り立つaを探索する
# なお、m=2N/nとしたとき、m−n=2a−1となるため、
# m−nが奇数であることが必要
# 2Nの正の約数dであって、dと2N/dの偶奇が異なるようなももの個数を求める

def div(M):
    res = set()
    i = 1
    while(i*i <= M):
        if M%i == 0:
            res.add(i)
            res.add(M//i)
        i += 1
    return res

N =int(input())

D = div(2*N)

ans = 0
for n in D:
    m = (2*N)//n
    # n, mの偶奇の判定
    if (n-m)%2 == 1:
        ans += 1
print(ans)
