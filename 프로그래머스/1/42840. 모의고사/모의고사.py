def solution(answers):
    one = [1,2,3,4,5]*2000
    two = [2,1,2,3,2,4,2,5]*1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] *1000
    onec=0
    twoc=0
    threec=0
    
    for i in range(len(answers)):
        if answers[i] == one[i]:
            onec += 1
        if answers[i] == two[i]:
            twoc += 1
        if answers[i] == three[i]:
            threec += 1
    mc = max(onec,twoc)
    mc = max(mc,threec)
    
    answer = []
    if mc == onec:
        answer.append(1)
    if mc == twoc:
        answer.append(2)
    if mc == threec:
        answer.append(3)
    return answer