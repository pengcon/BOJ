import sys
input= sys.stdin.readline
N=int(input())
swithcs=list(map(int,input().split()))
swithcs=[-1]+swithcs
S=int(input())

def man(num):
    for i in range(num,len(swithcs),num):
        swithcs[i]=(swithcs[i]+1)%2
def women(num):
    swithcs[num]=(swithcs[num]+1)%2
    left=num-1
    right=num+1
    while True:
        if left<0 or right>=len(swithcs):
            break
        elif swithcs[left]!= swithcs[right]:
            break
        else:
            swithcs[left]=(swithcs[left]+1)%2
            swithcs[right]=(swithcs[right]+1)%2
            left-=1 
            right+=1      
        
        
def printing():
    for i in range(1,len(swithcs)):
        if i%20==0:
            print(swithcs[i])
        else:
            print(swithcs[i],end=' ')
        

for _ in range(S):
    gender,num=map(int,input().split())
    if gender==1:
        man(num)
    else:
        women(num)

printing()
        