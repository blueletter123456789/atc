n, q = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

score_asc = [0]*(n+1)
for i, a in enumerate(lst):
    score_asc[i+1] += (score_asc[i] + a)

for _ in range(q):
    x = int(input())
    ans = 0

    st, fi = 0, n-1
    while st <= fi:
        te = (st+fi) // 2
        if lst[te] < x:
            st = te + 1
        else:
            fi = te - 1
    ans = x*st
    ans -= score_asc[fi+1]
    ans += score_asc[n] - score_asc[st]
    ans -= x * (n - st)

    print(ans)
