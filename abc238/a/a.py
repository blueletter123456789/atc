import math

n = int(input())
a = n**2
a = math.log2(a) 
if n > a:
    print('Yes')
else:
    print('No')
