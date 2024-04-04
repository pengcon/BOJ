N,X=map(int,input().split())
nums=list(map(int,input().split()))

nums.sort()

count=0

remain=0


while(True):
    if len(nums)>0 and nums[-1]==X:
       count+=1
       nums.pop()
    else:
        break 
start=0
end=len(nums)-1

while(start<=end):

    if start==end:
        remain+=1
        break

    elif 2*(nums[start]+nums[end])>=X:
        start+=1
        end-=1
        count+=1

    else:
        start+=1
        remain+=1
print(count+(remain//3))