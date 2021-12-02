n = int(input())
l = list(map(int, input().split()))
cnt = 0
while all(i%2==0 for i in l):
    cnt += 1
    l = [j/2 for j in l]
print(cnt)
