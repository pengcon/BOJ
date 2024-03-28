n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]



garo_dp = [[0 for _ in range(n)]for _ in range(n)]
sero_dp = [[0 for _ in range(n)]for _ in range(n)]
daegak_dp =[[0 for _ in range(n)]for _ in range(n)]

garo_dp[0][1]=1

# print(graph)

#좌 상 상좌
dx=[0,-1,-1]
dy=[-1,0,-1]

for i in range(2,n):
    if graph[0][i]==0 and graph[0][i-1]==0:
        garo_dp[0][i]=garo_dp[0][i-1]
for x in range(1,n):
    for y in range(1,n):
        if garo_dp[x][y]==0 and sero_dp[x][y]==0 and daegak_dp[x][y]==0:
            if 0<=x+dx[0]<n and 0<=y+dy[0]<n:
                #왼쪽에서 오는 애
                if graph[x][y]==0:
                    garo_dp[x][y]=garo_dp[x+dx[0]][y+dy[0]]+daegak_dp[x+dx[0]][y+dy[0]]
            if 0<=x+dx[1]<n and 0<=y+dy[1]<n:
                #위에서 오는 애
                if graph[x][y]==0:
                    sero_dp[x][y]=sero_dp[x+dx[1]][y+dy[1]]+daegak_dp[x+dx[1]][y+dy[1]] 
            if 0<=x+dx[2]<n and 0<=y+dy[2]<n:
                if graph[x][y]==0 and graph[x][y-1]==0 and  graph[x-1][y]==0:
                    #대각선에서 오는 애
                    daegak_dp[x][y]=garo_dp[x+dx[2]][y+dy[2]]+sero_dp[x+dx[2]][y+dy[2]]+daegak_dp[x+dx[2]][y+dy[2]]
# print(garo_dp)
# print(sero_dp)
# print(daegak_dp)
print(garo_dp[n-1][n-1]+sero_dp[n-1][n-1]+daegak_dp[n-1][n-1])

