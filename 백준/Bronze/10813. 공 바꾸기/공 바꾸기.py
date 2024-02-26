n,m=map(int,input().split())
n_list=[i for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    n_list[a],n_list[b]=n_list[b],n_list[a]
for i in range(1,len(n_list)):
    print(n_list[i],end=' ')