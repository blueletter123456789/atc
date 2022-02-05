n = input()
ans = 0
for i in range(len(n)-1):
    s = int(n[i])
    min_n = 10**(i)-1
    max_n = 10**(i+1)-1
    a = (max_n*(max_n+1)//2)-(min_n*(min_n+1)//2)
    ans += a
ans += (int(n)%max_n)*((int(n)%max_n)+1)//2
print(ans%998244353)
