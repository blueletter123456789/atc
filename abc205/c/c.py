def solved(a, b, c):
    if c == 0:
        return '='
    if c % 2 == 0:
        if abs(a) == abs(b):
            return '='
        elif abs(a) > abs(b):
            return '>'
        else:
            return '<'
    else:
        if a == b:
            return '='
        elif a > b:
            return '>'
        else:
            return '<'

# Sample code
# def solved(a, b, c):
#     if c % 2 == 0:
#         a *= a
#         b *= b
#     if a == b:
#         return '='
#     elif a > b:
#         return '>'
#     else:
#         return '<'

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    
    print(solved(a, b, c))

