a, b = map(int, input().split())
if a == b:
    c = b
else:
    c = (a-b)/3 + b
print(c)
