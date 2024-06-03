R,C,T=map(int,input().split())
arr=[list(map(int,input().split())) for  _ in range(R)]
plus=[[0 for _ in range(C)] for _ in range(R)]
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cleaner=[]
ans=0
# 청정기 위 아래 입력
for i in range(R):
    if arr[i][0]==-1:
        cleaner.append([i,0])
        cleaner.append([i+1,0])
        break

def diffusion(x,y):
    diffusion_count=0
    diffusion_mist=arr[x][y]//5
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<R and 0<=ny<C and arr[nx][ny]!=-1:
            diffusion_count += 1
            plus[nx][ny] += diffusion_mist
    arr[x][y]=arr[x][y]-(diffusion_count*diffusion_mist)

def up_clean(x,y):
    #청정기 위의 먼지 제거
    x=x-1
    arr[x][y]=0
    #위로
    while x>=1:
        arr[x][y]=arr[x-1][y]
        x=x-1
    #오른쪽으로
    while y<=C-2:
        arr[x][y]=arr[x][y+1]
        y=y+1
    #아래로
    while x<=cleaner[0][0]-1:
        arr[x][y]=arr[x+1][y]
        x=x+1
    #왼쪽으로
    while y>=2:
        arr[x][y]=arr[x][y-1]
        y=y-1
    #청정기 오른쪽 먼지 제거
    arr[x][y]=0
def down_clean(x,y):
    #청정기 아래의 먼지 제거
    x=x+1
    arr[x][y]=0
    #아래로
    while x<=R-2:
        arr[x][y]=arr[x+1][y]
        x=x+1
    #오른쪽으로
    while y<=C-2:
        arr[x][y]=arr[x][y+1]
        y=y+1
    #위로
    while x>=cleaner[1][0]+1:
        arr[x][y]=arr[x-1][y]
        x=x-1
    #왼쪽으로
    while y>=2:
        arr[x][y]=arr[x][y-1]
        y=y-1
    #청정기 오른쪽 먼지 제거 (수정)
    arr[x][y]=0

for _ in range(T):
        
    #1번 확산
    for j in range(R):
        for k in range(C):
            if arr[j][k]>0:
                diffusion(j,k)
    for j in range(R):
        for k in range(C):
            arr[j][k] += plus[j][k]
    #2번 공기청정기 순환 -> 반시계
    up_clean(cleaner[0][0],cleaner[0][1])
    down_clean(cleaner[1][0],cleaner[1][1])
    plus=[[0 for _ in range(C)] for _ in range(R)]
for l in arr:
    ans += sum(l)
print(ans+2)