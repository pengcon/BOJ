from collections import defaultdict
calender=defaultdict(int)
N=int(input())
for _ in range(N):
    n1, n2 = map(int,input().split())
    for i in range(n1,n2+1):
        calender[i]+=1

new=True
start=0
max_schedule=0
ans=0
for i in range(1,366):

    if calender[i]>0 and new==True:
        start=i
        new = False
        
    if calender[i]==0 and new==False:
        #넓이
        ans+=(i-start)*max_schedule
        new = True
        max_schedule = 0
    elif max_schedule<calender[i]:
        max_schedule=calender[i]

    if i==365 and new == False:
        ans+=(i-start+1)*max_schedule
print(ans)