def solution(numbers):
    ans = []
    visited =set()
    num_len = len(numbers)
    def back(n): 
        if len(n)>=1 and len(n) <= num_len:
            ans.append(n)
        for i in range(num_len):
            if i not in visited:
                visited.add(i)
                back(n+numbers[i])
                visited.remove(i)
    back("")
    print(ans)  
    answer = set()
    print(10%2)
    for i in ans:
        temp = int(i)
        if temp <= 1:
            continue
        flag = False
        for j in range(2,temp):
            if temp % j == 0:
                flag = True
                break
        if flag: continue
        answer.add(temp)
    print(answer)
    return len(answer)