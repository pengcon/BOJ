from collections import deque
#상 하 좌 우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
# N=x N=y
N,M=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
remain_cheese=0
last_chesee=0
ans_count=0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            remain_cheese += 1

while remain_cheese>0:
    air=set()
    visited=set()
    q= deque()
    q.append([0,0])
    visited.add((0,0))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if (nx,ny) not in visited and arr[nx][ny]==0:
                    q.append([nx,ny])
                    visited.add((nx,ny))
                elif (nx,ny) not in air and arr[nx][ny]==1:
                    air.add((nx,ny))
    for x,y in air:
        arr[x][y]=0
    last_chesee=len(air)
    remain_cheese -= last_chesee
    ans_count += 1
print(ans_count)
print(last_chesee)

