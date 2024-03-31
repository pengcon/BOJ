yes="yes"
no="no"
while(True):
    a=input()
    if a=="0":
        break
    else:
        a=list(a)
    for i in range(len(a)):
        if a[i]!=a[len(a)-1-i]:
            print(no)
            break
        if i==len(a)-1:
            print(yes)