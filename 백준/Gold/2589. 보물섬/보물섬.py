from collections import deque
sero,garo=map(int,input().split())
graph=[list(input().rstrip()) for i in range(sero)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

bomul=-1

def bfs(x,y):
    visited=[[False for i in range(garo)] for j in range(sero)]
    q=deque([[x,y,0]])
    visited[x][y]=True
    # print(q)
    max_count=0
    while q:
        cur=q.popleft()
        
        
        # print(q)
        # print(cur)
        if max_count<cur[2]:
            max_count=cur[2]
        for i in range(4):
            nx=dx[i]+cur[0]
            ny=dy[i]+cur[1]
            if 0<=nx<sero and 0<=ny<garo and visited[nx][ny]==False and graph[nx][ny]=='L':
                visited[nx][ny]=True
                q.append([nx,ny,cur[2]+1])
    return max_count
            
        
for i in range(sero):
    for j in range(garo):
        if graph[i][j]=='L':
            count=bfs(i,j)
            if bomul<count:
                bomul=count
print(bomul)
    