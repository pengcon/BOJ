from collections import deque
N,K=map(int,input().split())
durability=list(map(int,input().split()))
q=deque()
for i in range(2*N):
    #내구도와 로봇 유무
    q.append([durability[i],False])
stop=False
ans=0
while not stop:
    #단계 증가
    ans+=1
    # 1번 회전
    q.appendleft(q.pop())
    # 내리는 위치 확인
    if q[N-1][1]==True:
        q[N-1][1]=False
    # 2번 로봇 자체 이동
    if q[N-2][1]==True and q[N-1][0]>0:
        q[N-2][1] = False
        q[N-1][0] -= 1
    for i in range(N-3,-1,-1):
        if q[i][1]==True and q[i+1][0]>0 and q[i+1][1]==False:
            q[i][1]=False
            q[i+1][0] -=1
            q[i+1][1]=True
    #3번 올리는 위치 로봇
    if q[0][0]>0 and q[0][1]==False:
        q[0][0] -=1
        q[0][1] = True
    # 4번 내구도 0 체크
    zero_count=0
    for j in range(2*N):
        if q[j][0]==0:
            zero_count += 1
    if zero_count>=K:
        stop=True
print(ans)
