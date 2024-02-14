t=int(input())
for _ in range(t):
    i=0
    a=list(input())
    while(True):

        if len(a)==0:
            print("YES")
            break            
        if i==int(len(a)-1):
            print("NO")
            break
        if a[i]+a[i+1]=="()":
            a.pop(i)
            a.pop(i)
            i=0
        else:
            i=i+1