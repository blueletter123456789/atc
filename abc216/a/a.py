n = float(input())
n *= 10
if n % 10 <= 2:
    print(str(int(n//10)) + '-')
elif n % 10 <= 6:
    print(str(int(n//10)))
else:
    print(str(int(n//10)) + '+')
