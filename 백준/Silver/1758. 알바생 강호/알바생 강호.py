import sys
input = sys.stdin.readline
n=int(input())
n_list=[]
sum=0
for i in range(n):
    n_list.append(int(input()))
n_list.sort(reverse=True)

for i in range(n):
    temp=n_list[i]-i
    if temp>0:
        sum+=temp
print(sum)