n = int(input())
l = [int(i) for i in input().split()]
l.sort(reverse=True)
a = b = 0
for i in range(0,n,2):
    a += l[i]
    if i+1 < n:
        b += l[i+1]
print(a-b)
