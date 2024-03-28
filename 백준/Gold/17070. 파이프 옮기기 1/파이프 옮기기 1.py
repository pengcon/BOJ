n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]


#가로 세로 대각선 DP 생성 
garo_dp = [[0 for _ in range(n)]for _ in range(n)]
sero_dp = [[0 for _ in range(n)]for _ in range(n)]
daegak_dp =[[0 for _ in range(n)]for _ in range(n)]

#초기의 파이프에 대한 dp 생성
garo_dp[0][1]=1

# print(graph)

#좌 상 상좌 (파이프를 움직일 때 사용)
dx=[0,-1,-1]
dy=[-1,0,-1]

# 1열은 다 0이니까 graph[][]이 인덱스 오버가 나지 않게
# 1행만 따로 처리
# 따로안해두면 if문 개많이쓰고(x가0이고 y가0이지않을때,x가0이고y가0일때 등등..) 
# 각각 경우마다 continue 해야함
# 근데 그래놓고 오답뜸 그냥 이렇게 하세요 쓰러지기 싫으면
for i in range(2,n):
    if graph[0][i]==0 and graph[0][i-1]==0:
        garo_dp[0][i]=garo_dp[0][i-1]

# x y를 1부터 n까지
for x in range(1,n):
    for y in range(1,n):
        #dp가 모두 0일때 -> 한번도 방문하지 않았을 때 + dp가 들렸을수도 있지만 값은 0일 때 
        if garo_dp[x][y]==0 and sero_dp[x][y]==0 and daegak_dp[x][y]==0:

            #왼쪽에서 오는 애 -> 자기 그래프값이 0이면 됨
            if graph[x][y]==0:
                #왼쪽의 가로dp, 대각선dp  가져옴
                garo_dp[x][y]=garo_dp[x+dx[0]][y+dy[0]]+daegak_dp[x+dx[0]][y+dy[0]]
            

            #위에서 오는 애 -> 자기 그래프값이 0이면 됨
            if graph[x][y]==0:
                #위의 세로dp, 대각선dp 가져옴
                sero_dp[x][y]=sero_dp[x+dx[1]][y+dy[1]]+daegak_dp[x+dx[1]][y+dy[1]] 
           

            #대각선에서 오는 애 ->자기랑,자기왼쪽,윗쪽 그래프의 값이 다 0 이여야 됨
            if graph[x][y]==0 and graph[x][y-1]==0 and  graph[x-1][y]==0:
                #대각선의 가로,세로,대각선dp 다 가져옴
                daegak_dp[x][y]=garo_dp[x+dx[2]][y+dy[2]]+sero_dp[x+dx[2]][y+dy[2]]+daegak_dp[x+dx[2]][y+dy[2]]

#마지막 구석자리의 가로,세로,대각선dp값 합친거 출력
print(garo_dp[n-1][n-1]+sero_dp[n-1][n-1]+daegak_dp[n-1][n-1])

