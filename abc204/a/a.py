def solved():
    # (6 - x -y) % 3でもok
    if x == y:
        return x
    return 3 - (x + y)

if __name__ == '__main__':
    x, y = map(int, input().split())

    print(solved())
