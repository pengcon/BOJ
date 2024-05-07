n=int(input())
s=0
e=n
mid=(s+e)//2
while s<=e:
    if mid**2==n:
        s=mid
        break
    elif mid**2<n:
        s=mid+1
    elif mid**2>n:
        e=mid-1
    mid=(s+e)//2
print(s)