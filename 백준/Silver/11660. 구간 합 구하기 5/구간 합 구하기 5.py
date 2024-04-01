import sys
input=sys.stdin.readline

n,m=map(int,input().split())
num_list=[[0]*(n+1)]
for i in range(n):
    temp_list=[0]+list(map(int,input().split()))
    num_list.append(temp_list)
prefix_sum=[[0 for i in range(n+1)] for j in range(n+1)]


for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j]=prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+num_list[i][j]

 
for i in range(m):
    i,j,x,y=map(int,input().split())
    print(prefix_sum[x][y]-prefix_sum[i-1][y]-prefix_sum[x][j-1]+prefix_sum[i-1][j-1])        