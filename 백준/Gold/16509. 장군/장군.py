from collections import deque

def bfs(dx,dy,start,visited,count):
    q=deque([[start[0],start[1],count]])
    # print(q)
    visited[start[0]][start[1]]=True
    while q:
        v= q.popleft()
        # dx,dy 횟수만큼 빙빙돌아
        for i in range(8):
            block=False
            x=v[0]
            y=v[1]
            # print(x,y)
            for j in range(3):
                # print(i,j,dx[i][j])
                x=x+dx[i][j]
                y=y+dy[i][j]
                if x==kingx and y==kingy and j !=2:
                    block=True
            if block==True:
                continue
            # if x>=0 and x<10 and y>=0 and y<9:
            #     print(x,y,v[2])
            if x>=0 and x<10 and y>=0 and y<9 and visited[x][y]==False:
                if x==kingx and y==kingy:
                    # print("찾았다")
                    return v[2]
                else:
                    q.append([x,y,v[2]+1])
                    visited[x][y]=True

    return -1           
            



#세로,가로
n=10
m=9

#방문여부
visited=[[False]*m for _ in range(n)]

#상,왕의 x,y
sangx,sangy=map(int,input().split())
kingx,kingy=map(int,input().split())

#횟수
count=1
#정답 횟수
ans=0

#상좌,상우,하좌,하우,좌상,좌하,우상,우하
dx=[[-1,-1,-1], [-1,-1,-1], [1,1,1], [1,1,1], [0,-1,-1], [0,1,1], [0,-1,-1], [0,1,1]]
dy=[[0,-1,-1], [0,1,1], [0,-1,-1], [0,1,1], [-1,-1,-1], [-1,-1,-1], [1,1,1], [1,1,1]]

#bfs 시작 지점
start=[sangx,sangy]
print(bfs(dx,dy,start,visited,count))