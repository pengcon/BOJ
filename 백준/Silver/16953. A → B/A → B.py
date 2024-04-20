from collections import deque
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
    temp=cur*10+1
    if temp<=B:
        q.append((temp,count+1))
    #2를 곱해줌
    if cur*2<=B:
        q.append((cur*2,count+1))
if ans==1e9:
    print(-1)
else:
    print(ans)