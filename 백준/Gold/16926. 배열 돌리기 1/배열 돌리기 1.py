# 2:43
from collections import deque
import sys
input=sys.stdin.readline
N,M,R=map(int,input().split())

nums=[list(map(int,input().split())) for _ in range(N)]
ans=[[-1 for _ in range(M)] for _ in range(N)]
#시계방향으로 배열을 담음
x_min=0
y_min=0 
x_max=N-1
y_max=M-1
while (x_max > x_min and y_max >y_min):
    temp=deque()
    #위 배열
    for i in range(y_min,y_max+1):
        temp.append(nums[x_min][i])
    #오른쪽 배열
    for j in range(x_min+1,x_max):
        temp.append(nums[j][y_max])
    #아래 배열
    for k in range(y_max,y_min-1,-1):
        temp.append(nums[x_max][k])
    #왼쪽 배열
    for l in range(x_max-1,x_min,-1):
        temp.append(nums[l][y_min])

    temp.rotate(-R)

    #위 배열
    for i in range(y_min,y_max+1):
        ans[x_min][i] = temp.popleft()
    #오른쪽 배열
    for j in range(x_min+1,x_max):
        ans[j][y_max] = temp.popleft()
    #아래 배열
    for k in range(y_max,y_min-1,-1):
        ans[x_max][k] = temp.popleft()
    #왼쪽 배열
    for l in range(x_max-1,x_min,-1):
        ans[l][y_min] = temp.popleft()
    x_min+=1
    y_min+=1
    x_max-=1
    y_max-=1
for i in ans:
    print(*i)