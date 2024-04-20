from collections import deque
import sys
input=sys.stdin.readline
A,B=map(int,input().split())
ans=1e9
 
q=deque()
q.append((A,1))

while q:
    cur,count=q.popleft()
    if cur == B:
        ans=min(ans,count)
        break
    #오른쪽에 1을 추가하기 위함
    temp1=cur*10+1
    temp2=cur*2
    if temp1<=B:
        q.append((temp1,count+1))
    #2를 곱해줌
    if temp2<=B:
        q.append((temp2,count+1))
if ans==1e9:
    print(-1)
else:
    print(ans)