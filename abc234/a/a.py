def func(n):
    return n**2 + 2*n + 3

def main(n):
    s = func(func(func(n) + n) + func(func(n)))
    print(s)

if __name__ == '__main__':
    n = int(input())
    main(n)
