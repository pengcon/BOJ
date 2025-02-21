from collections import deque
def solution(priorities, location):
    answer = 0
    count = 0
    dq = deque()
    sorted_pri = sorted(priorities)
    for i in range(len(priorities)):
        dq.append((i,priorities[i]))
    while(len(dq)>0):
        process = dq.popleft()
        if process[1]<sorted_pri[-1]: #우선순위가 작으면 
            dq.append(process)
        else:
            sorted_pri.pop()
            count +=1
            if process[0] == location:
                answer = count
                break
    return answer