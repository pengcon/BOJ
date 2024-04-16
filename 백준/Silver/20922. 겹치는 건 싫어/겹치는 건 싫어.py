N,K=map(int,input().split())
nums=list(map(int,input().split()))
num_dict={}
start=0
end=0
length=0
ans=0
while(end<N):
    if nums[end] in num_dict.keys():
        if num_dict[nums[end]]>=K:
            num_dict[nums[start]]-=1
            start+=1
            length-=1
        else:
            num_dict[nums[end]]+=1
            ans=max(ans,end-start+1)
            end+=1
            length+=1
    else:
        num_dict[nums[end]]=1
        ans=max(ans,end-start+1)
        end+=1
        length+=1

print(ans)