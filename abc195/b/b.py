a, b, w = map(int, input().split())
w *= 1000

dp_small = [float('inf') for _ in range(w+1)]
dp_large = [-float('inf') for _ in range(w+1)]

dp_small[0], dp_large[0] = 0, 0
for i in range(w-a+1):
    if i >= a:
        dp_small[i] = min(dp_small[i], dp_small[i-a]+1)
        dp_large[i] = max(dp_large[i], dp_large[i-a]+1)
    if i >= b:
        dp_small[i] = min(dp_small[i], dp_small[i-b]+1)
        dp_large[i] = max(dp_large[i], dp_large[i-b]+1)

ans_small, ans_large = float('inf'), -float('inf')

for i in range(w-b, w-a+1):
    ans_small = min(ans_small, dp_small[i]+1)
    ans_large = max(ans_large, dp_large[i]+1)

if ans_small == float('inf') or ans_large == -float('inf'):
    print('UNSATISFIABLE')
else:
    print(ans_small, ans_large)


#### Sample code ###
# import math

# a, b, w = map(int, input().split())
# w *= 1000

# upper = math.floor(w/a)
# bottom = math.ceil(w/b)
# if bottom > upper:
#     print('UNSATISFIABLE')
# else:
#     print(bottom, upper)
