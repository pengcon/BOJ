from collections import deque
from itertools import permutations
import sys
input=sys.stdin.readline
n=int(input())





max_score=-1


batter=[list(map(int,input().split())) for _ in range(n)]

entry=[i for i in range(1,9)]


for i in permutations(entry,8):
    

    next=0

    #스코어
    score=0

    temp=list(i)
    #4번타자 슬라이싱으로 넣어줌
    temp=temp[:3]+[0]+temp[3:]


    # 다음 타자 순서 맞추기
    # if next!=0:
    #     temp=temp[next:]+temp[0:next]
    for j in range(n):
        #1루 주자
        b1=0
        #2루 주자    
        b2=0
        #3루 주자
        b3=0

        out_count=0

        while out_count<3:


            if batter[j][temp[next]]==0:
                out_count+=1
            #1루타
            if batter[j][temp[next]]==1:
                score +=b3
                b1,b2,b3=1,b1,b2
                # if b3==1:
                #     score+=1
                #     b3=0
                # if b2==1:
                #     b2=0
                #     b3=1
                # if b1==1:
                #     b2=1
                #     b1=0
                # b1=1
            elif batter[j][temp[next]]==2:
                score+=b2+b3
                b1,b2,b3=0,1,b1
                # if b3==1:
                #     score+=1
                #     b3=0
                # if b2==1:
                #     score+=1
                #     b2=0
                # if b1==1:
                #     b3=1
                #     b1=0
                # b2=1
            elif batter[j][temp[next]]==3:
                score+=b1+b2+b3
                b1,b2,b3=0,0,1
                # if b3==1:
                #     score+=1
                #     b3=0
                # if b2==1:
                #     score+=1
                #     b2=0
                # if b1==1:
                #     score+=1
                #     b1=0
                # b3=1
            elif batter[j][temp[next]]==4:
                score+=b1+b2+b3+1
                b1,b2,b3=0,0,0
                # if b3==1:
                #     score+=1
                #     b3=0
                # if b2==1:
                #     score+=1
                #     b2=0
                # if b1==1:
                #     score+=1
                #     b1=0
                # score+=1
            #다음 타자 갱신
            if next==8:
                next=0
            else:
                next+=1

                    
    if max_score<score:
        max_score=score
print(max_score)