n= int(input())
dic = {}
for i in range(n-1):
    a,b= map(int,input().split())
    if dic.get(a) == None:
        dic[a] = [b]
    else: 
        dic[a].append(b)
    if dic.get(b) == None:
        dic[b] = [a] 
    else:
        dic[b].append(a)
q = int(input())
for j in range(q):
    t,k = map(int,input().split())
    if t == 1:
        if len(dic[k])>1:
            print("yes")
        else:
            print("no")
    elif t == 2:
            print("yes")