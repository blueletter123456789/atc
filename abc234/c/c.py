def main(n):
    s = str(bin(n))[2:]
    a = ''
    for i in s:
        if i == '1':
            a += '2'
        else:
            a += '0'
    print(int(a))

if __name__ == '__main__':
    n = int(input())
    main(n)
