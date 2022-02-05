n = input()
int_n = int(n)
ans = 0
for i in range(len(n)):
    min_n = 10**(i)
    max_n = min(10**(i+1), int_n+1)
    ans += (max_n-min_n)*((max_n-min_n)+1)//2
print(ans%998244353)
