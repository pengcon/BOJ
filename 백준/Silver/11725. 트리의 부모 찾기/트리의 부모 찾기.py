from collections import deque


n=int(input())
graph = [[]for i in range(n+1)]
# mom = [[]for i in range(n+1)]



def dfs(graph,start):
    visited=[]
    dq=deque()
    mom = [0 for i in range(n+1)]
    dq.append(start)

    while dq:
        node=dq.pop()


        visited.append(node)
        for i in graph[node]:
            if mom[i] ==0:
                mom[i]=node
                dq.append(i)

    return  mom

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
mom=dfs(graph,1)
for i in range(2,n+1):
    print(mom[i])


