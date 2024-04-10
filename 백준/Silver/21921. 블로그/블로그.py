X,N=map(int,input().split())
visit_list=list(map(int,input().split()))

prefix=[visit_list[0]]
for i in range(1,X):
    prefix.append(prefix[i-1]+visit_list[i])
start=0
end=N
max_sum=prefix[N-1]
max_count=1
for i in range(1,X-(N-1)):
    new=prefix[end]-prefix[start]
    if max_sum<new:
        max_sum=new
        max_count=1
    elif max_sum==new:
        max_count+=1       
    start+=1
    end+=1
if max_sum==0:
    print("SAD")
else:
# print(prefix)///x)
    print(max_sum)
    print(max_count)