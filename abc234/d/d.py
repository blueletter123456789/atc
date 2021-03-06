# def main(n, k, l):
#     for i in range(k, n+1):
#         t = sorted(l[:i], reverse=True)
#         print(t[k-1])
 
# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     l = list(map(int, input().split()))
#     main(n, k, l)

import heapq
N,K = map(int,input().split())
P = list(map(int,input().split()))
que = P[0:K]
print(min(que))
heapq.heapify(que)
for i in range(K,N):
    minima = heapq.heappop(que)
    minima = max(minima,P[i])
    heapq.heappush(que,minima)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que,ans)