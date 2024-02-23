num=int(input())
n=[0]*int(num+1)
n[1]=0
for i in range(2,num+1):
    count=9999
    if i%3==0:
        count=n[i//3]+1
    if i%2==0 and n[i//2]+1<count:
        count=n[i//2]+1
    if n[i-1]+1<count:
        count=n[i-1]+1
   
    n[i]=count
    # print("n["+str(i)+"] = "+str(n[i]))
print(n[num])