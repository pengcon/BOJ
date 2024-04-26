N=int(input())
first,second,third=(map(int,input().split()))
maxs=[first,second,third]
mins=[first,second,third]
for i in range(N-1):
    one,two,three=map(int,input().split())
    max0,max1,max2=maxs
    min0,min1,min2=mins
    maxs[0]=max(max0+one,max1+one)
    # print("max[0]:"+str(maxs[0]))
    maxs[1]=max(max0+two,max1+two,max2+two)
    # print("max[1]:"+str(maxs[1]))
    maxs[2]=max(max1+three,max2+three)
    # print("max[2]:"+str(maxs[2]))
    mins[0]=min(min0+one,min1+one)
    # print("max[0]:"+str(maxs[0]))
    mins[1]=min(min0+two,min1+two,min2+two)
    mins[2]=min(min1+three,min2+three)

print(max(maxs),end=" ")
print(min(mins))
