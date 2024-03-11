alpha=[chr(i) for i in range(65,91)]
value=[3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
a=input()
value_list=[]
for i in a:
    for j in range(len(alpha)):
        if alpha[j]==i:
            value_list.append(value[j])
while len(value_list) != 1:
    temp_list=[]
    length=len(value_list)
    if length%2==0:
        for i in range(0,length,2):
            temp_list.append((value_list[i]+value_list[i+1])%10)
    else:
        for i in range(0,length-1,2):
            temp_list.append((value_list[i]+value_list[i+1])%10)
        temp_list.append(value_list[length-1])
    value_list=temp_list
if value_list[0]%2==0:
    print("You're the winner?")
else:
    print("I'm a winner!")