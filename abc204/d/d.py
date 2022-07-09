def solved():
    # lst.sort(reverse=True)
    total = sum(lst)
    dp = [[False]*(total//2+1) for i in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(total//2+1):
            dp[i+1][j] = dp[i][j]
            if j < lst[i]:
                continue
            if dp[i][j-lst[i]]:
                dp[i+1][j] = True
    
    idx = 0
    for i in range(total//2 + 1):
        if dp[n][i]:
            idx = i
    return total - idx

if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))

    print(solved())
