people=int(input())
num_list=[]
start=0
count=0
for i in range(people):
    num_list.append(list(map(int,input().split())))

num_list.sort(key=lambda x:x[0])
num_list.sort(key=lambda x:x[1])
while(len(num_list)!=0):
    if start<=num_list[0][0]:
        start=num_list[0][1]
        num_list.pop(0)
        count+=1
    else:
        num_list.pop(0)
print(count)
    