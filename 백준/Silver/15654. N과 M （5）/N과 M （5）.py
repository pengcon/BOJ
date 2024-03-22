def recur(number,output):
    if number == M:
        print(output)
        return
    
    for i in N_list:
        if i not in arr:
            arr.append(i)
            recur(number+1,output+str(i)+" ")
            arr.pop()
            
N,M=map(int,input().split())
N_list=list(map(int,input().split()))
N_list.sort()
arr=[]
recur(0,"")