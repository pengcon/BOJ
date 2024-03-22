def solution(numbers, target):
    global answer
    answer = 0
    def dfs(idx,num_sum):
        global answer
        if idx==len(numbers):
            if num_sum==target:
                answer+=1
            return
        dfs(idx+1,num_sum+numbers[idx])
        dfs(idx+1,num_sum-numbers[idx])
    dfs(0,0)
    return answer

