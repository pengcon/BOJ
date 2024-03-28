dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    if dp[x][y]!=0:
        return dp[x][y]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if 0<=nx<n and 0<=ny<n:
            if graph[x][y] < graph[nx][ny]:
                dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]
    
n= int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)]for _ in range(n)]
#모든 점 방문

#방문한 뒤에 이동할 수 있는 모둔 경우의 수를 재귀로 구현

#재귀 구현 뒤 dp로 바꾼다.

for x in range(n):
    for y in range(n):
        dfs(x,y)
# print(dp)
print(max(map(max,dp))+1)
