n = int(input())
l = list()
l.append('1')
for i in range(1, n):
    l.append(str(l[i-1]) + ' ' + str(i+1) + ' ' + str(l[i-1]))
print(l[n-1])
