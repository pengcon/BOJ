import sys,copy
input= sys.stdin.readline
T=int(input())

for i in range(T):
    n,angle=map(int,input().split())
    turn = 0
    mid=((n+1)//2)
    lists=[]
    for i in range(n):
        lists.append(list(map(int,input().split())))
    
    #각에 대한 회전횟수
    if angle>0:
        # if angle>180:
        #     turn=-(360-angle)//45
        # else:
            turn=angle//45
    elif angle<0:
        # if angle<-180:
        #     turn=(360-angle)//45
        # else:
            turn= angle//45
    #회전 진행
    if turn>0:
        for i in range(turn):
            #새로만들 리스트 복사
            new_lists=copy.deepcopy(lists)
            
        #주대각 가운대행
            for j in range(n):
                new_lists[j][mid-1]=lists[j][j]
        
        #가운대행 부대각
            for j in range(n):
               new_lists[j][n-1-j] =lists[j][mid-1]

        #부대각 가운대열
            for j in range(n):
                new_lists[mid-1][j]=lists[n-1-j][j]
        #가운데열 주대각
            for j in range(n):
                new_lists[j][j]=lists[mid-1][j]
            lists=new_lists


    elif turn <0:
        for i in range(-turn):
            #새로만들 리스트 복사
            new_lists=copy.deepcopy(lists)

        #주대각 가운데열
            for j in range(n):
                new_lists[mid-1][j]=lists[j][j]

        #가운데열 부대각
            for j in range(n):
                new_lists[n-1-j][j]=lists[mid-1][j]

        #부대각 가운대행
            for j in range(n):
                new_lists[j][mid-1]=lists[j][n-1-j]

        #가운대행 주대각
            for j in range(n):
                new_lists[j][j]=lists[j][mid-1]
            lists=new_lists

    for k in lists:
        print(*k)