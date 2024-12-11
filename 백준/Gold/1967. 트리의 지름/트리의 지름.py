from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = {}

for i in range(n-1):
    a,b,c = list(map(int,input().split()))
    if a not in graph:
        graph[a]=([[b,c]])
    else:
        graph[a].append([b,c])
    if b not in graph:
        graph[b]=([[a,c]])
    else:
        graph[b].append([a,c])
ans = 0
ans_idx=-1
def dfs(start):
    answer= 0 
    answer_idx = -1
    visited = set()
    visited.add(start)
    nv = deque()
    nv.append([start,0])
    while nv:
        now,count = nv.pop()
        for k in graph[now]:
            if k[0] not in visited:
                visited.add(k[0])
                nv.append([k[0],count+k[1]])
                if answer < count+k[1]:
                    answer = count+k[1]
                    answer_idx=k[0]
    return answer,answer_idx
if n==1:
    print(0)
else:
    ans,ans_idx = dfs(1)
    ans,ans_idx = dfs(ans_idx)
    print(ans)
