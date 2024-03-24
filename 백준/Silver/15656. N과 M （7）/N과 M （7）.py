import sys
input = sys.stdin.readline
def recur(number,output):
    if number == M:
        
        print(output)
        # num_list.append(arr.copy())
        return
    
    for i in N_list:
            arr.append(i)
            recur(number+1,output+str(i)+" ")
            arr.pop()
            
N,M=map(int,input().split())
N_list=list(map(int,input().split()))
N_list.sort()
arr=[]
# num_list=[]
recur(0,"")