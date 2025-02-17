def solution(progresses, speeds):
    answer = []
    date = []
    max_num = 0
    count = 0
    for i in range(len(speeds)):
        date.append(((100-progresses[i]) + (speeds[i]-1)) // speeds[i])
        
    for i in date:
        if max_num == 0:
            count += 1
            max_num = i
        elif max_num < i:
            max_num = i
            answer.append(count)
            count=1
        else:
            count += 1
    if count>0:
        answer.append(count)

    return answer