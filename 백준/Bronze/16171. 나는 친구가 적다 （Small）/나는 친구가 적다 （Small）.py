n=list(input()) # 1q2w
answer=input() #qwerty
ans_list=[]
for i in n:
    if i.isalpha():
        ans_list.append(i)
alpha=""
for i in ans_list:
    alpha+=i
# print(alpha)
if answer in alpha :
    print(1)
else: print(0)