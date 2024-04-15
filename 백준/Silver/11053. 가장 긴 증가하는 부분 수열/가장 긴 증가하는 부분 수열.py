import sys
input=sys.stdin.readline
N=int(input())
lists=list(map(int,input().split()))

dp=[1 for i in range(N)]
dp[0]=1
if N>1:
    if lists[1]>lists[0]:
        dp[1]=dp[0]+1
    else:
        dp[1]=dp[0]
for i in range(2,N):
    temp_dp=1
    for j in range(i):
        if lists[j]<lists[i]:
            temp_dp=max(dp[j]+1,temp_dp)
    dp[i]=temp_dp
print(max(dp))