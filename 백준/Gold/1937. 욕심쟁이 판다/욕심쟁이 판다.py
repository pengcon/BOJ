from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
bamboo_list=[]
max_move=0
for i in range(n):
    temp_list=list(map(int,input().split()))
    bamboo_list.append(temp_list)

dp=[[0 for i in range(n)] for j in range(n)]  

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y]=1
    # 현재 노드와 연결된 다른 노드를 재귀적(스택 기반)으로 방문
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and bamboo_list[x][y]<bamboo_list[nx][ny]:
            dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

for i in range(n):
    for j in range(n):             
        max_move=max(max_move,dfs(i,j))
print(max_move)