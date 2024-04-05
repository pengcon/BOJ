
import sys 
input=sys.stdin.readline
N,M=map(int,input().split()) 
trees=list(map(int,input().split()))

start=0
end=max(trees)

ans=-1
while(start<=end):
    mid=(start+end)//2
    sum=0
    for i in trees:
        if i-mid>0: 
            sum+=(i-mid) 
    # print(sum,M)            
    if sum==M:
        ans=mid
        break
    elif sum>M: 
        ans=mid
        start=mid+1
    else:
        end=mid-1
    # print(start,end)    
print(ans)
        
        
