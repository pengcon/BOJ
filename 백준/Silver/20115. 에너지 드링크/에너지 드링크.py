import sys
input=sys.stdin.readline
n=int(input())
n_list=list(map(int,input().strip().split()))
default=max(n_list)
n_list.sort()
# print(n_list)
for i in range(n-1):
    default+=n_list[i]/2
if default-int(default)==0:
    print(int(default))
else:
    print(default)


