n,m=map(int,input().split())
lst = list(map(int,input().split()))
temp=[]
ans=0
def back(idx,cnt):
    global ans
    if sum(temp)==m and cnt>0:
        ans+=1
    if cnt==n:
        return 
    for i in range(idx,n):
        temp.append(lst[i])
        back(i+1,cnt+1)
        temp.pop()
back(0,0)
print(ans)