import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
link=[ []for i in range(N+1)]

for _ in range(M):
    B,A=map(int,input().split())
    link[A].append(B)


def bfs(i):

    temp_max=0
    q=deque([i])
    visited = list(map(lambda x: 0, range(N+1)))
    visited[i]=1
    while q:
        node=q.popleft()
        for j in link[node]:
            if not visited[j]:
                visited[j] = 1
                q.append(j)
                temp_max+=1
    return temp_max

ans=[]
for i in range(1,N+1):
    ans.append(bfs(i))

high=max(ans)
for k in range(N):
    if ans[k]==high:
        print(k+1,end=" ") 