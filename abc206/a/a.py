from decimal import Decimal

n = int(input())
price = int(n*Decimal('1.08'))
if price == 206:
    print('so-so')
elif price < 206:
    print('Yay!')
else:
    print(':(')
