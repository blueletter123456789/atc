from decimal import Decimal

def main(n, m):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i < j < k:
                    s = abs((m[j][0]-m[i][0])*(m[k][1]-m[i][1])-(m[k][0]-m[i][0])*(m[j][1]-m[i][1]))/2
                    if s != 0:
                        cnt += 1
                    # if m[i][0] == m[j][0] and m[i][0] != m[k][0]:
                    #     cnt += 1
                    # elif m[i][0] != m[j][0] and m[i][0] == m[k][0]:
                    #     cnt += 1
                    # elif m[i][0] == m[j][0] and m[i][0] == m[k][0]:
                    #     continue
                    # elif (Decimal(str(m[i][1]-m[j][1]))/Decimal(str(m[i][0]-m[j][0])) 
                    #     != Decimal(str(m[i][1]-m[k][1]))/Decimal(str(m[i][0]-m[k][0]))):
                    #     cnt += 1
    print(cnt)

if __name__ == '__main__':
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    main(n, m)