y,x=map(int,input().split())
a=[]
for i in range(y):
    a.append([])
    b=input()
    for j in b:
        a[i].append(j)
warray=[]
barray=[]
for i in range(8):
    if i%2==0:
        warray.append([])
        c='WBWBWBWB'
        for j in c:
            warray[i].append(j)
    elif (i%2)!=0:
        warray.append([])
        c='BWBWBWBW'
        for j in c:
            warray[i].append(j)

for i in range(8):
    if i%2!=0:
        barray.append([])
        c='WBWBWBWB'
        for j in c:
            barray[i].append(j)
    elif (i%2)==0:
        barray.append([])
        c='BWBWBWBW'
        for j in c:
            barray[i].append(j)
xroll=x-7
yroll=y-7
count=0
maxcount=64
for h in range(yroll):
    for i in range(xroll):
        
        for j in range(h,h+8):
            for k in range(i,i+8):
                 
                if a[j][k]!=warray[j-h][k-i]:
                    count+=1
        if maxcount>count: maxcount=count
        count=0                
        
        for j in range(h,h+8):
            for k in range(i,i+8):
                 
                   
                if a[j][k]!=barray[j-h][k-i]:
                    
                    count+=1
        if maxcount>count: maxcount=count
        count=0

print(maxcount)