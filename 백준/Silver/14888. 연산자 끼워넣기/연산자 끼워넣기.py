n=int(input())
nums = list(map(int,input().split()))
lst = list(map(int,input().split()))

max_ans = -2e9
min_ans = 2e9
def back(temp,cnt):
    global max_ans
    global min_ans
    if cnt == n-1:
        max_ans = max(temp, max_ans)
        min_ans = min(temp, min_ans)
        return 
    for i in range(4):
        if lst[i]>0:
            lst[i]-=1
            if i == 0:
                back(temp+nums[cnt+1],cnt+1)
            elif i == 1:
                back(temp-nums[cnt+1],cnt+1)
            elif i == 2:
                back(temp*nums[cnt+1],cnt+1)
            elif i == 3:
                back(int(temp/nums[cnt+1]),cnt+1)
            lst[i]+=1
back(nums[0],0)
print(max_ans)
print(min_ans)