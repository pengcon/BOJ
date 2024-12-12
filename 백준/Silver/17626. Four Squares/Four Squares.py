dp =[0 for _ in range(50001)]
dp[1]=1
dp[2]=2
dp[3]=3
dp[4]=1

n = int(input())
for i in range(5,n+1):
    ans = 5
    mid = int(i**0.5)
    if mid**2 ==i:
        dp[i] = 1
    else:
        for j in range(mid,0,-1):
            ans = min(ans,1+dp[i-j**2])
            dp[i] = ans

print(dp[n])
