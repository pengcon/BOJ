""" 
< 와 > 가 k개(2 ≤ k ≤ 9) 순서열 A
앞뒤에 한자릿수 숫자로 부등호 만족.
k개 부등호 순서를 만족하는
k+1자리의 정수중 최댓값과 최솟값 찾기.


입력)
첫 줄에 k (부등호 개수)
둘째줄에 부등호 모양

0<1 <2 <3 <4 <5 <6 <7 <8 <9

1.맨 윗자리 할당.

1-1.최댓값을 할 때.
높은자리수 큰 수 우선
넣을 때 다음 부등호를 봄
부등호의 < 개수만큼 최댓값 감소
그다음 >으로 바뀌는 곳에 최댓값
반복
ex)
< < < > < < > < >   ->    6 <7 <8 < 9 >4 <5 >2 <3 >1 

1-2.최솟값을 할 때.
높은자리수 낮은 수 우선
넣을 때 다음 부등호를 봄
부등호의 >개수만큼 최소값 증가
> < < < > > > < <    ->  1> 0 < 2<3 < 7>6 >5 >4 <8 <9

"""
visited=[]
ans=[]
n=int(input())
sign_list=list(map(str, input().split()))

def check(left, right, sign):
    if sign == '<':
        return left < right
    else:
        return left > right
    
def back(count,temp):
    if count==n+1:
        a=""
        for i in temp:
            a=a+str(i)
        ans.append(a)
        # ans.append(temp.copy())
        return
    
    
    for i in range(10):
        if i not in visited:
            if count == 0 or check(temp[-1],i,sign_list[count-1]):
                visited.append(i)
                temp.append(i)
                back(count+1,temp)
                visited.pop()
                temp.pop()

back(0,[])

print(ans[-1])
print(ans[0])