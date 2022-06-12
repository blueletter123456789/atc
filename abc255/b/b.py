import math

def dist(x1, y1, x2, y2):
    return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

n, k = map(int, input().split())
l_lst = list(map(int, input().split()))
points = [tuple(map(int, input().split())) for _ in range(n)]

max_dist = 0
for i, val in enumerate(points):
    x, y = val
    min_dist = 10**10
    for person in l_lst:
        if person == i+1:
            min_dist = 0
            break
        x2, y2 = points[person-1]
        min_dist = min(min_dist, dist(x, y, x2, y2))
    max_dist = max(max_dist, min_dist)

print(max_dist)
