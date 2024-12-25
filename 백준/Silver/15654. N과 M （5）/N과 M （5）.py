n,m = map(int,input().split())

lst=list(map(int,input().split()))
lst.sort()
ans=[]

def back(cnt):
    if cnt == m:
        print(*ans)
        return
    for i in lst:
        if i not in ans:
            ans.append(i)
            back(cnt+1)
            ans.pop()
back(0)