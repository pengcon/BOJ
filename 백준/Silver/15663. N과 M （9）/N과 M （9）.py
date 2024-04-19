n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
#딕셔너리 활용
nd={}
for i in nums:
    if i not in nd.keys(): 
        nd[i]=1
    else:
        nd[i]+=1
temp = []
visited=[]
def dfs(idx):
    if len(temp) == m:
        print(*temp)

        return
    for i in nd.keys():
        if nd[i]!=0:
            nd[i]-=1
            temp.append(i)
            dfs(idx+1)
            nd[i]+=1
            temp.pop()  

dfs(0)