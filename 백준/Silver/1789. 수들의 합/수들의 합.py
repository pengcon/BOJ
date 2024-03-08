def binary_search(start,end,n,answer):
    if start>end:
        return answer
    mid=(start+end)//2
    sum=(mid*(mid+1))//2
   
    if sum>n:
        return binary_search(start,mid-1,n,mid-1)
    else:
        return binary_search(mid+1,end,n,answer)
n=int(input())
print(binary_search(0,n,n,1))