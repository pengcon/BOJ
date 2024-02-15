# from collections import deque
# queue=deque()
n_list=[]
del_list=[]
n,k=list(map(int,input().split()))
count=k-1
for i in range(1,n+1):
    n_list.append(i)
while(len(n_list)!=0):
    del_list.append(n_list[count])
    del n_list[count]
    if len(n_list)!=0:
        count=(count+k-1)%len(n_list)
print("<",end='')
for i in range(len(del_list)):
    print(del_list[i],end='')
    if i != len(del_list)-1:
        print(",",end=' ')


print(">")