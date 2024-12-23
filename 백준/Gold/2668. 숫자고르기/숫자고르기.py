from collections import defaultdict

n=int(input())

dict = defaultdict(list)

def dfs(x, visited):
    visited.add(x)
    checked[x] = 1
    for v in dict[x]:
        if v not in visited:
            dfs(v, visited.copy())
        else: 
            ans.extend(list(visited))
            return
        
for i in range(1,n+1):
    v = int(input())
    dict[v].append(i)

checked = [0 for _ in range(n+1)]
ans = []

for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set([]))

ans.sort()
print(len(ans)) 
for i in ans:
    print(i)
 