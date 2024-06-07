def solution(n):
    answer = 0
    #완탐
    #1부터 n까지
    for i in range(1,n+1):
        hap=0
        #i부터 n까지
        for j in range(i,n+1):
            #연속된 자연수들을 더해감 (i+(i+1)+(i+2) ...)
            hap = hap + j
            # 합이 n보다 크면 for문을 중단하고 다음수부터 시작 ((i+1)+(i+2)+(i+3)...)
            if hap>n:
                break
            # 합과 n이 같으면 정답을 증가시켜줌
            elif hap==n:
                answer += 1
    return answer