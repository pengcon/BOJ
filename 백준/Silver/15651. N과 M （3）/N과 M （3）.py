n,m = map(int,input().split())

lst=[]
def back(cnt):
    if cnt == m:
        print(*lst)
        return
    for i in range(n):
        lst.append(i+1)
        back(cnt+1)
        lst.pop()
back(0)