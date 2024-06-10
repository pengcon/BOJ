def match(num):
    if num % 2 ==0:
        return num // 2
    else:
        return (num // 2) + 1
    
def solution(n,a,b):
    answer = 0
    round = 1
    while (n>0):
        if match(a) == match(b):
            answer = round
            break
        else:
            a = match(a)
            b = match(b)
            round += 1
    
    return answer