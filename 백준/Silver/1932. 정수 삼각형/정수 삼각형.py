n=int(input())
lists=[]
dp=[[0 for i in range(n)] for j in range(n)]

for _ in range(n):
    lists.append(list(map(int,input().split())))

dp[0][0]=lists[0][0]
for i in range(n-1):
    for j in range(len(lists[i])):
        dp[i+1][j]=max(dp[i][j]+lists[i+1][j],dp[i+1][j])
        dp[i+1][j+1]=max(dp[i][j]+lists[i+1][j+1],dp[i+1][j+1])
print(max(dp[n-1]))       