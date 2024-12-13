from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m=map(int,input().split())
lst=[]
zero_count = 0 
for i in range(m):
    temp_lst= list(map(int,input().split()))
    zero_count += temp_lst.count(0)
    lst.append(temp_lst)
dq = deque()
for i in range(m):
    for j in range(n):
        if lst[i][j] == 1:
            dq.append([i,j,0])

visited = set()
ans = 0
while dq:
    x,y,d = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and [nx,ny] and lst[nx][ny]==0 and (nx,ny) not in visited:
            dq.append([nx,ny,d+1])
            visited.add((nx,ny))
            zero_count-=1
            ans = max(ans,d+1)
if zero_count>0:
    print(-1)
else:
    print(ans)