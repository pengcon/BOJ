n=int(input())
sum=[0,1]

i=2
while(True):
    if n==1:
        print(1) 
        break
    if n==2:
        print(1) 
        break
    
    sum.append(sum[i-1]+i)

    if sum[i]==n:
       
        print(i)
        break
    elif sum[i-1]<n<sum[i]:
       
        print(i-1)
        break
    i+=1
# sum[2]=3 sum[3]=6
# n=5면  sum[2]<n<sum[3]