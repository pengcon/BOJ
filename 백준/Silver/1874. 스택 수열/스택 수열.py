n=int(input())
visited=[0]*int(n+1)
num_list=[]
ans_list=[]
max=0
for i in range(n):
    
    now=int(input())
    # print(num_list)
    if max<now:
        for j in range(max+1,now):
            if visited[j]==0:
                num_list.append(j)
                ans_list.append("+")
        ans_list.append("+")
        ans_list.append("-")
        visited[now]==1
        max=now
    elif max>=now:
        if num_list[-1]!=now:
            ans_list.clear()
            ans_list.append("NO")

        else:
            visited[num_list.pop()]==1
            ans_list.append("-")
if ans_list[0]=="NO":
    print("NO")
else: 
    for i in ans_list:
        print(i)