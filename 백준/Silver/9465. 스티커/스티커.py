import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    stickers=[]
    n=int(input())
    for i in range(2):
        temp=list(map(int,input().split()))
        stickers.append(temp)
    
    dp=[[0 for i in range(n)],[0 for i in range(n)]]
    dp[0][0]=stickers[0][0]
    dp[1][0]=stickers[1][0]
    if n>1:
        dp[0][1]=dp[1][0]+stickers[0][1]
        dp[1][1]=dp[0][0]+stickers[1][1]

    for i in range(2,n):
        for j in range(0,2):
            a=dp[1-j][i-1]+stickers[j][i]
            b=dp[1-j][i-2]+stickers[j][i]
            dp[j][i]=max(a,b)
    print(max(dp[1][-1],dp[0][-1]))