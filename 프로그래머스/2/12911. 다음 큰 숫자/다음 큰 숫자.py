def solution(n):
    def count_one(num):
        count = 0
        while(num>=1):
            count += num % 2
            num = num // 2
        return count
    answer = 0
    num = n + 1
    find_ans = False
    
    while not find_ans:
        if count_one(n) == count_one(num):
            answer = num
            find_ans = True
        else:
            num += 1
            
    return answer