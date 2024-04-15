import sys
input=sys.stdin.readline
N=int(input())
arr=[list(map(str, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
user=[list(map(str, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

mine_loc=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]=="*":
            mine_loc.append([i,j])


def find_mine(x,y):
    #지뢰 개수
    mine_count=0
    #위부터 시계방향으로
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if arr[nx][ny]=="*":
                mine_count+=1
    return mine_count

mine_flag=False
for i in range(N):
    for j in range(N):
        if user[i][j]=="x":
            if arr[i][j]=="*":
                mine_flag=True
            else:
                user[i][j]=find_mine(i,j)
        else: user[i][j]="."
if mine_flag==True:
    for i,j in mine_loc:
        user[i][j]="*"
for i in user:
    for j in i:
        print(j,end='')
    print()