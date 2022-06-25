from collections import namedtuple
import math

Point = namedtuple('Point', ['x', 'y'])

def based_origin(lst, idx):
    bx, by = lst[idx]
    return [Point(p.x-bx, p.y-by) for p in lst]

def dist(p1, p2):
    return (p1.x-p2.x)**2 + (p1.y-p2.y)**2

def rot(lst, theta):
    ret = list()
    for x, y in lst:
        xi = x*math.cos(theta) + y*-math.sin(theta)
        yi = x*math.sin(theta) + y*math.cos(theta)
        ret.append(Point(xi, yi))
    return ret

def is_same(s, t):
    for ps in s:
        same = False
        for pt in t:
            if abs(ps.x-pt.x) < 0.01 and abs(ps.y-pt.y) < 0.01:
                same = True
                break
        if not same:
            return False
    
    return True

def solved():
    if n == 1:
        return True
    
    based_s = based_origin(S, 0)
    r = dist(S[0], S[1])
    theta_s=math.atan2(based_s[1].y,based_s[1].x)

    for i in range(n):
        for j in range(n):
            if dist(T[i], T[j]) != r:
                continue
            based_t = based_origin(T, i)
            theta_t = math.atan2(based_t[j].y, based_t[j].x)
            rot_s = rot(based_s, theta_t-theta_s)
            if is_same(rot_s, based_t):
                return True

if __name__ == '__main__':
    n = int(input())
    S = list()
    T = list()
    for _ in range(n):
        a, b = map(int, input().split())
        S.append(Point(a, b))
    for _ in range(n):
        a, b = map(int, input().split())
        T.append(Point(a, b))

    is_same = solved()
    if is_same:
        print('Yes')
    else:
        print('No')


# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# n = int(input())

# S = [None]*n
# T = [None]*n
# BS = [list() for _ in range(n)]
# BT = [list() for _ in range(n)]

# for i in range(n):
#     a, b = map(int, input().split())
#     S[i] = Point(a, b)
# for i in range(n):
#     a, b = map(int, input().split())
#     T[i] = Point(a, b)

# xs, ys = S[0]
# xt, yt = T[0]
# for i in range(1, n):
#     for j in range(i, n):
#         xi, yi = S[i]
#         xj, yj = S[j]
#         BS[i].append((xi-xs)*(xj-xs) + (yi-ys)*(yj-ys))
#         # BS[i].append(xi*xj + yi*yj)
#         xi, yi = T[i]
#         xj, yj = T[j]
#         BT[i].append((xi-xt)*(xj-xt) + (yi-yt)*(yj-yt))
#         # BT[i].append(xi*xj + yi*yj)

# flg = True
# for i in range(n):
#     for sb, tb in zip(BS[i], BT[i]):
#         print(sb, tb, sb-tb)
#         if sb != tb:
#             flg = False
#             break

# if flg:
#     print('Yes')
# else:
#     print('No')
