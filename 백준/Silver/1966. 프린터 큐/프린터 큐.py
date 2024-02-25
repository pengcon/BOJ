from collections import deque
t=int(input())
for _ in range(t):
    count=0
    n,m=list(map(int,input().split()))
    mark=deque([False]*n)
    mark[m]=True
    n_list=deque(map(int,input().split()))
    while(True):
        if max(n_list)==n_list[0]:
            n_list.popleft()
            count+=1
            if mark.popleft()==True:
                break
        else: 
            n_list.append(n_list.popleft())
            mark.append(mark.popleft())
    print(count)
            
