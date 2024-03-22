def recur(number,output,min):
    if number == M:
        print(output)
        return
    
    for i in range(1,N+1):
        if i>=min:
            recur(number+1,output+str(i)+" ",i)
        
N,M=map(int,input().split())

recur(0,"",0)