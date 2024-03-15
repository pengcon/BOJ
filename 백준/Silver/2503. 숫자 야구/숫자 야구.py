import sys
input = sys.stdin.readline
t=int(input())
ans=[]
num_list=[]
strike_list=[]
ball_list=[]
all=[]
for i in range(1,10):    
    for j in range(1,10):      
        for k in range(1,10):
            a=""
            if i!=j and j!=k and i!=k:
                a=a+str(i)+str(j)+str(k)
                all.append(a)
for i in range(t):
    num,strike,ball=map(int,input().split())
    num_list.append(str(num))
    strike_list.append(strike)
    ball_list.append(ball)
for i in all:
    for j in range(t):
        strike=0
        ball=0
        for k in range(3): 
            if i[k]==num_list[j][k]:
                strike+=1
            elif i[k] in num_list[j]:
                ball+=1
        if strike_list[j]!=strike or ball_list[j]!=ball:
            break
        if j==t-1:
            ans.append(i)
# print(ans)
print(len(ans))