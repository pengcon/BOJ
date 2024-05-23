from collections import defaultdict
def solution(N, stages):
    answer = []
    #디폴트 딕셔너리
    dodal = defaultdict(int)
    fail = defaultdict(int)
    fail_rate=[]
    #사람 전체 스테이지 도달 
    for i in stages:
        fail[i]+=1
    dodal[N+1]=fail[N+1]
    for l in range(N,0,-1):
        dodal[l]=fail[l]+dodal[l+1]
    
    for j in range(N,0,-1):
        if dodal[j]==0:
            fail_rate.append([0,j])
        else:
            fail_rate.append([(fail[j]/dodal[j]),j])
    fail_rate.sort(key = lambda x : (-x[0],x[1]))
    for k in range(N):
        answer.append(fail_rate[k][1])
    return answer