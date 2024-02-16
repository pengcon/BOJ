str_list=list(map(str,input().split('.')))
can=True
for i in str_list:
    if len(i)%2!=0:
        print(-1)
        can=False
        break
if can==True:    
    for i in range(len(str_list)):
        a=len(str_list[i])//4
        b=len(str_list[i])%4
        for _ in range(a):
            print("AAAA",end='')
        for _ in range(b):
            print("B",end='')
        if i!=len(str_list)-1:
            print(".",end='')        