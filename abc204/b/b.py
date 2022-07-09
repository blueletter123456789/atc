def solved():
    nuts = 0
    for i in lst:
        if i <= 10:
            continue
        nuts += i - 10
    return nuts


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))

    print(solved())
