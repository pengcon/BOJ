n,m = map(int,input().split())

lst=list(map(int,input().split()))
lst.sort()
lst = set(lst)
ans=[]

ansans=[]
def back(cnt):
    if cnt == m:
        ansans.append(ans.copy())
        return
    for i in lst:
        ans.append(i)
        back(cnt+1)
        ans.pop()
back(0)
ansans.sort()
for a in ansans:
    print(*a)