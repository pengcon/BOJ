while(True):
    n = int(input())
    if n == -1:
        break
    root = int(n**0.5)
    answer_set= set()
    answer_set.add(1)
    for i in range(2,root+1):
        if n % i == 0:
            answer_set.add(i)
            answer_set.add(n // i)
    answer = str(n)
    answer_set = list(answer_set)
    answer_set.sort()
    if sum(answer_set) == n :
        answer += " = "
        for j in range(0,len(answer_set)):
            if j == len(answer_set) - 1:
                answer += str(answer_set[j])
            else:
                answer += str(answer_set[j])+ " + "
    else:
        answer += " is NOT perfect." 
    print(answer)