def main(s):
    if len(s) == 1:
        print(s)
        print(s)
        return
    l = []
    for i in range(len(s)):
        l.append(s[i:]+s[:i])
    print(min(l))
    print(max(l))

if __name__ == '__main__':
    s = input()
    main(s)
