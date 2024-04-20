
N,M=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
arr=[]
visited=[]
def recur(idx):
    # print(visited)
    if len(arr)==M:
        if arr not in visited:
            visited.append([arr[j] for j in range(len(arr))])
            print(*arr)
        return
    for i in range(max(0,idx-1),len(nums)):
        arr.append(nums[i])
        recur(i+1)
        arr.pop()
    return
recur(0)