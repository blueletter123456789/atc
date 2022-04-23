from collections import defaultdict
import heapq

INF = 1000000007

t = int(input())
for _ in range(t):
    n = int(input())
    rl = defaultdict(list)
    min_num = INF
    for i in range(n):
        l, r = map(int, input().split())
        # 下限に格納許容の上限を追加
        rl[l].append(r)
    # 格納許容のインデックスの上限を設定
    st_idx = 0
    # 下限のリストを作成しソート
    st = [i for i in rl]
    st.append(INF)
    st.sort()
    # 格納対象のインデックスの下限を取得
    tgt_idx = st[0]
    h = list()
    is_ok = True
    next_val = st[st_idx]
    while st_idx < len(st)-1:
        st_idx += 1
        next_val = st[st_idx]
        for r in rl[tgt_idx]:
            heapq.heappush(h, r)
        while len(h) > 0 and next_val > tgt_idx:
            num = heapq.heappop(h)
            if num < tgt_idx:
                is_ok = False
                break
            # 箱に入れたら格納対象のインデックスをインクリメント
            tgt_idx += 1
        tgt_idx = next_val
    if is_ok:
        print('Yes')
    else:
        print('No')
