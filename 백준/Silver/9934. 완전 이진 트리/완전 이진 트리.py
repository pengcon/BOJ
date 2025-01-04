from collections import deque
n=int(input())
max_count= 2**n-1
lst = list(map(int,input().split()))
lst = deque(lst)
ans = [-1 for i in range(max_count)]

def back(n):
    if n>=max_count:
        return
    back(2*n + 1)
    ans[n] = lst.popleft()
    back(2*n + 2)
back(0)

for i in range(n):
    for j in range(2**i-1,2**(i+1)-1):
        print(ans[j], end=' ')
    print()