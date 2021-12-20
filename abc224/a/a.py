def main(s):
    if s[-2:] == 'er':
        return 'er'
    else:
        return 'ist'

if __name__ == '__main__':
    s = input()
    print(main(s))