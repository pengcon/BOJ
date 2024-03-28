import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]



def dfs(x,y):
    count=0
    if dp[x][y]!=-1:
        return dp[x][y]    
    if x==n-1 and y==m-1:
        return 1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if 0<=nx<n and 0<=ny<m:
            if graph[x][y]>graph[nx][ny]:
                count+=dfs(nx,ny)
    dp[x][y] = count
    return dp[x][y]
                

n,m= map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dp = [[-1 for _ in range(m)]for _ in range(n)]

dfs(0,0)
# print(dp)
print(dp[0][0])
