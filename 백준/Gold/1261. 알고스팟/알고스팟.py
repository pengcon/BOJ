import sys
import heapq
input=sys.stdin.readline
 
 
dx=[-1,1,0,0]
dy=[0,0,-1,1]

M,N=map(int,input().split())
arr=[]
for i in range(N):
    temp=input().strip()
    temp_arr=[]
    for j in temp:
        temp_arr.append(int(j))
    arr.append(temp_arr)
dist = [[1e9 for i in range(M)] for j in range(N)]
dist[0][0]=0

# visited = [[False for _ in range(M)] for _ in range(N)]

#bfs
q = []
#거리,x,y
heapq.heappush(q,[0,0,0])

min_weight=1e9
while q:
    #우선순위 큐로 거리보고 정렬
    weight,x,y =heapq.heappop(q)

    # if x==N-1 and y==M-1:
        # min_weight=min(min_weight,weight)
    #4방 배열
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if dist[nx][ny]>dist[x][y]+arr[nx][ny]:
                # print(dist[x][y],arr[nx][ny])
                dist[nx][ny]=dist[x][y]+arr[nx][ny]
                heapq.heappush(q,[weight,nx,ny])
# print(dist)
print(dist[N-1][M-1])