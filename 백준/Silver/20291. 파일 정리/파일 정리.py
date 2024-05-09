N=int(input())
D={}
for i in range(N):
    temp,end=input().split('.')
    if end in D.keys():
        D[end]+=1
    else:
        D[end]=1
keys=list(D.keys())
keys.sort()
for i in keys:
    print(f'{i} {D[i]}')