def calc(n):
    ret = 0
    for i, num in enumerate(reversed(x)):
        ret += (n**i) * int(num)
    return ret

def sovled():    
    base = 0
    for i in range(10):
        if str(i) in x:
            base = i

    left, right = base, m
    while right - left > 1:
        mid = (left + right) // 2
        # print(f'{left=}, {mid=}, {right=}')
        if calc(mid) <= m:
            left = mid
        else:
            right = mid

    print(left - base)


if __name__ == '__main__':
    x = input()
    m = int(input())

    sovled()


# TLE source code.
# def sovled():
#     if len(x) == 1:
#         print(m//int(x))
#         return
    
#     base = 0
#     for i in range(10):
#         if str(i) in x:
#             base = i + 1

#     cnt = 0
#     while True:
#         calc = 0
#         for i, num in enumerate(reversed(x)):
#             calc += (base**i) * int(num)
#         if calc > m:
#             break
#         cnt += 1
#         base += 1
#     print(cnt)


# if __name__ == '__main__':
#     x = input()
#     m = int(input())

#     sovled()
