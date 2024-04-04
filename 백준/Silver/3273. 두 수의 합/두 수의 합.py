N=int(input())
nums=list(map(int,input().split()))
ans=int(input())
nums.sort()
start=0
end=N-1
# print(nums)
count=0
while(start<end):
    temp_ans=nums[start]+nums[end]
    # print(temp_ans)
    if temp_ans==ans:
       count+=1
       start+=1
    elif temp_ans>ans:
        end-=1
    elif temp_ans<ans:
        start+=1
print(count) 