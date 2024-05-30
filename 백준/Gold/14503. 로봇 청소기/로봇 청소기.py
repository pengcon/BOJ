N,M=map(int,input().split())
robot_x,robot_y,robot_sight=map(int,input().split())
room=[list(map(int,input().split())) for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def move_robot_sight():
    global robot_sight
    if robot_sight==0:
        robot_sight=3
    else:
        robot_sight-=1

#로봇이 실행중일 때 
playing=True
ans=0
while playing:
    if visited[robot_x][robot_y]==0:
        visited[robot_x][robot_y]=1
        ans+=1
    check_not_clean=False
    for i in range(4):
        nx=robot_x+dx[i]
        ny=robot_y+dy[i]
        if room[nx][ny]==0 and visited[nx][ny]==0:
            check_not_clean=True
    if not check_not_clean:
        back_x=robot_x+dx[robot_sight-2]
        back_y=robot_y+dy[robot_sight-2]
        if room[back_x][back_y]==0:
            robot_x=back_x
            robot_y=back_y
        else:
            playing=False
    elif check_not_clean:
        move_robot_sight()
        front_x=robot_x+dx[robot_sight]
        front_y=robot_y+dy[robot_sight]
        if room[front_x][front_y]==0 and visited[front_x][front_y]==0:
            robot_x=front_x
            robot_y=front_y
print(ans)
