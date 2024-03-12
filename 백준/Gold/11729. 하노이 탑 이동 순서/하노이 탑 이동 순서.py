import sys
input= sys.stdin.readline
def move(num,start,arrive):
    temp_list=[]
    if num>1:
        for i in range(1,4):
            if i!=start and i!=arrive:
                temp_arrive=i
        a=move(num-1,start,temp_arrive)
        b=move(1,start,arrive)
        temp_list.append(b)
        c=move(num-1,temp_arrive,arrive)
        temp_list=a+b+c
    else:
      
        return [start,arrive]
    return temp_list

n=int(input())
answer_list=(move(n,1,3))
print(len(answer_list)//2)
for i in range(len(answer_list)//2):
    print(answer_list[2*i],end=' ')
    print(answer_list[2*i+1])