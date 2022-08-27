class SegmentTree(object):
    INF = -(1 << 17)

    def __init__(self, length):
        self.n = 1
        self.dat = list()
        self.length = length

        while self.n < length:
            self.n *= 2
        
        self.dat = [self.INF]*(2 * self.n - 1)
    
    def update(self, k, a):
        k += self.n - 1
        self.dat[k] = a

        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = max(self.dat[k*2+1], self.dat[k*2+2])
    
    def query(self, a, b):
        l = k = 0
        r = self.n
        def _query(a, b, k, l, r):
            if r <= a or b <= l:
                return self.INF
            
            if a <= l and r <= b:
                return self.dat[k]
            else:
                vl = _query(a, b, k*2+1, l, (l+r)//2)
                vr = _query(a, b, k*2+2, (l+r)//2, r)
                return max(vl, vr)
        return _query(a, b, k, l, r)

n = int(input())
st = SegmentTree(2**n)
idxs = dict()
for i, num in enumerate(list(map(int, input().split()))):
    idxs[num] = i+1
    st.update(i, num)

print(idxs[min(st.dat[1:3])])
