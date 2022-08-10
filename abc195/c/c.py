def solved(n):
    """
    1~999:            0
    1000~99999:       1
    1000000~99999999: 2
    ...
    """
    cnt = 0
    i = 0
    while 10**(3*(i+1)) <= n:
        cnt += (10**(3*(i+1)) - 10**(3*i))*i
        i += 1
    cnt += (n - (10**(3*i)) + 1)*i

    return cnt
        

if __name__ == '__main__':
    n = int(input())

    print(solved(n))

# n=int(input())
# ans=0

# if n>=1000: ans+=n-999
# if n>=1000000: ans+=n-999999
# if n>=1000000000: ans+=n-999999999
# if n>=1000000000000: ans+=n-999999999999
# if n>=1000000000000000: ans+=n-999999999999999

# print(ans)
