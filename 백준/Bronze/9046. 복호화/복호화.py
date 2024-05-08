N=int(input())
for i in range(N):
    lists=list(input().replace(" ",""))
    L=len(lists)
    D={}
    for i in range(L):
        if lists[i] in D.keys():
            D[lists[i]]+=1
        else:
            D[lists[i]]=1
    anss=[]
    for j in D.keys():
        anss.append([D[j],j])
    anss.sort(reverse=True)
    if len(anss)>1 and anss[0][0]==anss[1][0]:
        print("?")
    else:
        print(anss[0][1])