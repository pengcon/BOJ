def solution(n, arr1, arr2):
    answer=["" for _ in range(n)]
    def make_binary(num):
        binary=""
        for i in range(n):
            binary=str(num%2)+binary
            num=num//2
        return binary
    
    for i in range(n):
        temp1=make_binary(arr1[i])
        temp2=make_binary(arr2[i])
        
        for j in range(n):
            if temp1[j]=='0' and temp2[j]=='0':
                answer[i]=answer[i]+" "
            else:
                answer[i]=answer[i]+"#"
    return answer