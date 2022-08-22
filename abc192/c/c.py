def f1(x):
    return ''.join(sorted(list(x), reverse=True))

def f2(x):
    return ''.join(sorted(list(x)))

def g(x):
    return int(f1(x)) - int(f2(x))

n, k = input().split()

for i in range(int(k)):
    n = g(str(n))

print(n)
