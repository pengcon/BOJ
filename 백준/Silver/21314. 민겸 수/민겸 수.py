n = input()
num=''
ans_lst=[]

for i in n:
    num= num+i
    if i=='K':
        temp=1
        for j in num:
            if j =='M':
               temp= temp*10
            elif j=='K':
                temp = temp*5
        ans_lst.append(str(temp))
        num=''
if num!='':
    for i in num:
        ans_lst.append(str(1))
for i in ans_lst:
    print(i,end='')
print()

num=''
ans_lst=[]
for i in n:
    if i=='K':
        if len(num)>0:
            ans_lst.append(str(1*(10**(len(num)-1))))
            num=''
        ans_lst.append(str(5))
    elif i=='M':
        num=num+i
if len(num)>0:
    ans_lst.append(str(1*(10**(len(num)-1))))
    num=''  
for i in ans_lst:
    print(i,end='')