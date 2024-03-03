a,b=map(int,input().split())
list_a=list(map(int,input().split()))
list_b=list(map(int,input().split()))
list_c=[]
for i in list_a:
    list_c.append(i)
for i in list_b:
    list_c.append(i)
list_c=sorted(list_c)
for i in list_c:
    print(i,end=' ')