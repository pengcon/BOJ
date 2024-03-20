import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a_list=[]
b_list=[]
for i in range(m):
    a,b=map(int,input().split())
    a_list.append(a)
    b_list.append(b)
sejong=int(input())
manitto=0

count=n
if sejong not in a_list and sejong not in b_list:
    count= count-len(b_list)-1
elif sejong in a_list:
    count=1
elif sejong in b_list and sejong not in a_list:
    count=count-len(b_list)
    # for i in range(len(b_list)):
    #     if b_list[i]==sejong:
    #         manitto=a_list[i]
    # if manitto not in b_list:
    #     count=count-len(b_list)-1
    # elif manitto in b_list:
    #     count=count-len(b_list)
    for i in range(1,n+1):
        if i!=sejong and i not in a_list and i not in b_list and count==2:
            count-=1


if count>1:
    print(count)
else:
    print("NOJAM")