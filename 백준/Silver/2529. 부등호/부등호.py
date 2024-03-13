import sys
input = sys.stdin.readline

k=int(input()) #부등호 개수
mark = list(map(str, input().split())) # 부등호 입력받는거 ex < >
ans = []
visited=[]

#a는 왼쪽 숫자 b는 오른쪽숫자 c는 부등호
def check(left,sign,right):
    if sign == '<':
        return left < right # 0 < 1 
    else:
        return left > right
    
def back(count,temp_list):
    if count == k+1: # 배열의 길이를 확인
        a=""
        for i in temp_list:
            a=a+str(i)
        ans.append(a)
        # ans.append(temp.copy())
        return
    
   

    for i in range(10): # 0~9 까지 i=1
        if i not in visited: # 중복 확인 x
            if count==0 or check(temp_list[-1],mark[count-1],i): #  1,>,2 1>
                visited.append(i) #[0,1]
                temp_list.append(i) # [0,1]
                back(count+1,temp_list) # 재귀
                visited.pop()
                temp_list.pop()

back(0,[])
print(ans[-1]) #가장 작은수 
print(ans[0]) #가장 큰수 