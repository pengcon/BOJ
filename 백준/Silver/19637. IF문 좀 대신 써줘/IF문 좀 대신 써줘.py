import sys
input=sys.stdin.readline
def binary_Search(num,num_list):
    start=0
    end=len(num_list)-1
    answer=0
    while(start<=end):
        mid=(start+end)//2
        if num_list[mid][0]>=num:
            end=mid-1
            answer=mid
        else:
            start=mid+1
            
    return answer

n,m=list(map(int,input().split()))
chingho_list=[]

for i in range(n):
    name,power=list(map(str,input().split()))
    chingho_list.append([int(power),name])

# chingho_list.sort()

for i in range(m):
    a=int(input())
    print(chingho_list[binary_Search(a,chingho_list)][1])