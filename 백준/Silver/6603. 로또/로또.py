def backtracking(d,idx):
    if d==6 :
        print(*lst)
        return
    for i in range(idx,len):
            lst.append(n[i])
            backtracking(d+1,i+1)
            lst.pop()

while(True):
    n = list(map(int,input().split()))
    if n[0]==0:
        break
    len = n[0]
    n.pop(0)
    lst = []
    backtracking(0,0)
    print()