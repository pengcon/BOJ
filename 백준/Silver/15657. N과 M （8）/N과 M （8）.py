N,M=map(int,input().split())
N_list=sorted(list(map(int,input().split())))
arr=[]

def recur(number):
    if len(arr) == M:
        print(*arr) 
        return
    
    for i in range(number,N):
        arr.append(N_list[i])
        recur(i)
        arr.pop()
            

recur(0)