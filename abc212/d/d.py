import heapq

q = int(input())
l = list()
x_sum = 0
for _ in range(q):
    query = list(input().split())
    if int(query[0]) == 1:
        heapq.heappush(l, int(query[1])-x_sum)
    elif int(query[0]) == 2:
        x_sum += int(query[1])
    else:
        x = heapq.heappop(l)
        print(x+x_sum)
