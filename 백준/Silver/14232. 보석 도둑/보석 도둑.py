jewel=int(input())
ans_list=[]
stop=False
while(True):
    half=int(jewel**0.5)
    for i in range(2,half+1):
        if jewel%i==0:
            ans_list.append(i)
            jewel=jewel//i
            break
        if i==half:
            stop=True
            ans_list.append(jewel)
    if stop==True:break

print(len(ans_list))
for i in ans_list:
    print(i,end=' ')