def solution(n):
    answer = 0
    
    
    for i in range(1,n+1):
        hap=0
        for j in range(i,n+1):
            hap = hap + j
            if hap>n:
                break
            elif hap==n:
                answer += 1
    return answer