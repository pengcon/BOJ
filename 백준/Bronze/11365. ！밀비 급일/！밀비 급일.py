n_list=[]
while(True):
    temp=input()
    if temp=="END":
        break
    else:
        n_list.append(temp)
for i in range(len(n_list)):
    for j in range(len(n_list[i])-1,-1,-1):
        print(n_list[i][j],end='')
    print()
