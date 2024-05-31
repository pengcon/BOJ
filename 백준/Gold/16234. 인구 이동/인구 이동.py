from collections import deque
import sys
input=sys.stdin.readline
N,L,R = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
#상 하 좌 우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    visited[x][y]=True
    q.append([x,y])
    move=False
    link=[[x,y]]
    sum_people=arr[x][y]
    while q:
        r,c=q.popleft()
        for i in range(4):
            nx=r+dx[i]
            ny=c+dy[i]
            if 0<=nx<N and 0<=ny<N and L<=abs(arr[r][c]-arr[nx][ny])<=R and not visited[nx][ny]:
                move=True
                visited[nx][ny]=True
                q.append([nx,ny])
                link.append([nx,ny])
                sum_people+=arr[nx][ny]
    moved_people = sum_people//len(link)
    for j,k in link:
        arr[j][k]=moved_people
    return move

ans=0
while(True):
    visited=[[False for _ in range(N)] for _ in range(N)]
    move=0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                move=max(move,bfs(i,j))
    if move==0:
        break
    else:
        ans+=1
print(ans)