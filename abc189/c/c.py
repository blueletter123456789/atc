def largestRectangleArea(A):
    ans = 0
    A = [-1] + A
    A.append(-1)
    n = len(A)
    stack = [0]  # store index

    # 入力される数列分
    for i in range(n):
        # 数列の対象の要素が最後にみた最小の値と比較
        while A[i] < A[stack[-1]]:
            h = A[stack.pop()]
            # 対象の要素iがあることは保証されており、
            # 高さA[i]*(現在の要素-A[i]以上となるものの幅)
            area = h*(i-stack[-1]-1)
            ans = max(ans, area)
        stack.append(i)
    return ans


N=int(input())
A=list(map(int,input().split()))
print(largestRectangleArea(A))


# TLE source code
# class SegmentTreeRMQ(object):
#     INF = 1 << 17

#     def __init__(self, length):
#         self.n = 1
#         self.dat = list()
#         self.length = length

#         while self.n < length:
#             self.n *= 2
        
#         self.dat = [self.INF]*(2 * self.n - 1)
    
#     def update(self, k, a):
#         k += self.n - 1
#         self.dat[k] = a

#         while k > 0:
#             k = (k - 1) // 2
#             self.dat[k] = min(self.dat[k*2+1], self.dat[k*2+2])
    
#     def query(self, a, b):
#         l = k = 0
#         r = self.n
#         def _query(a, b, k, l, r):
#             if r <= a or b <= l:
#                 return self.INF
            
#             if a <= l and r <= b:
#                 return self.dat[k]
#             else:
#                 vl = _query(a, b, k*2+1, l, (l+r)//2)
#                 vr = _query(a, b, k*2+2, (l+r)//2, r)
#                 return min(vl, vr)
#         return _query(a, b, k, l, r)


# n = int(input())
# st = SegmentTreeRMQ(n)
# for i, num in enumerate(list(map(int, input().split()))):
#     st.update(i, num)

# ans = 0
# for i in range(n):
#     for j in range(i+1, n+1):
#         min_num = st.query(i, j)
#         ans = max(ans, min_num*(j-i))
# print(ans)



# Not correct code.
# def total(x):
#     ret = 0
#     tmp = 0
#     total_cnt = 0
#     for i in range(n):
#         if a[i] < x:
#             ret = max(ret, tmp)
#             total_cnt += tmp
#             tmp = 0
#         else:
#             tmp += x
#     return max(ret, tmp)

# n = int(input())
# a = list(map(int, input().split()))
# ma = max(a)

# ans = ma
# left, right = 0, ma
# while right - left > 1:
#     mid = (left + right) // 2
#     t = total(mid)
#     if t < ans:
#         left = mid
#     else:
#         right = mid
#     ans = max(ans, t)

# print(ans)
