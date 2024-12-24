from collections import defaultdict
import sys
input = sys.stdin.readline
limit_number = 15000
sys.setrecursionlimit(limit_number)
dic = defaultdict(list)

n,m = map(int,input().split())

for i in range(m):
    a,b= map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

ans=0
def dfs(x,visited,cnt):
    global ans
    visited[x] = True
    if cnt >= 4:
        ans = 1
        return
    visited[x] = True
    for i in dic[x]:
        if not visited[i]:
            dfs(i,visited,cnt+1)
    visited[x] = False

for i in range(n):
    visited = [False for _ in range(n)]
    dfs(i,visited,0)
    if ans == 1:
        print(ans)
        break
    if i==n-1:
        print(0)