n,m = map(int,input().split())

lst=list(map(int,input().split()))
lst.sort()
ans=[]
answered = []
r= len(lst)

def back(idx,cnt,r):
    if cnt == m:
        if ans not in answered: 
            answered.append(ans.copy())
            print(*ans)
            return
    
    for i in range(idx,r):
        ans.append(lst[i])
        back(i+1,cnt+1,r)
        ans.pop()

back(0,0,r)