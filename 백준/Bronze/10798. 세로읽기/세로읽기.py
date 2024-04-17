import sys
input=sys.stdin.readline
nums=[[-1 for _ in range(15)] for _ in range(5)]
for i in range(5):
    temps=list(map(str,input().rstrip()))
    idx=0
    for j in temps:
        nums[i][idx]=j
        idx+=1
for i in range(15):
    for j in range(5):
        if nums[j][i]!=-1:
            print(nums[j][i],end='')