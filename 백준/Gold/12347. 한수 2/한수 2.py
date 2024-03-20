n=int(input())
ans=[]
if n<=99:
    print(n)
else:
    ans=[i for i in range(1,100)]
    for i in range(1,10):
        for j in range(9):
            num=str(i)
            next=i+j
            while(True):
                if next>9:
                    break
                num=num+str(next)
                if int(num)>n:
                    break
                elif int(num) not in ans:
                    ans.append(int(num))
                next=next+j
    for k in range(1,10):
        for l in range(9):
            num=str(k)
            next=k-l
            while(True):
                if next<0:
                    break
                num=num+str(next) 
                # print(num)
                if int(num)>n:
                    break  
                elif int(num) not in ans:
                    ans.append(int(num))
                next=next-l
              
    print(len(ans))
    # print(ans)