#상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#배열 가로 세로
N=int(input())
#학생 리스트 생성
students = [list(map(int,input().split())) for  _ in range(N**2)]

#자리 리스트 생성 -> N+2만큼
arr=[[0 for _ in range(N+2)] for _ in range(N+2)]

#외곽은 -1로
for i in range(N+2):
    arr[0][i]=-1
    arr[N+1][i]=-1
    arr[i][0]=-1
    arr[i][N+1]=-1



#1번조건 -> 좋아하는 친구 찾기, 함수로 추출 할것
for student in students:
    friends=0
    max_one=0
    max_two=0
    check_one=[]
    check_two=[]
    check_three=[]
    ans=[]
    zero=0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j]==0:
                for k in range(4):
                    if arr[i+dx[k]][j+dy[k]] in student:
                        friends+=1
                #같으면 추가, 최대면 다 삭제하고 추가.
                if friends==max_one:
                    check_one.append([i,j])
                elif friends>max_one:
                    check_one=[[i,j]]
                    max_one=friends
                #친구 수 초기화
                friends=0
    #2번조건 -> 인접중에 비어있는 칸 많은곳을 찾기
    if len(check_one)==1:
        ans=check_one[0]
    elif len(check_one)>1:
        for i in check_one:
            for k in range(4):
                if arr[i[0]+dx[k]][i[1]+dy[k]]==0:
                    zero+=1
            if zero==max_two:
                check_two.append([i[0],i[1]])
            elif zero>max_two:
                check_two=[[i[0],i[1]]]
                max_two=zero
            zero=0
    #3번조건 -> 행(x)가 작고, 열(y) 가 작은 순서
    if len(check_two)==1:
        ans=check_two[0] 
        
    elif len(check_two)>1:

        check_three = sorted(check_two, key = lambda x : (x[0],x[1])) 
 
        for i in range(len(check_three)):
            if arr[check_three[i][0]][check_three[i][1]]==0:
                ans=check_three[i]
                break
    arr[ans[0]][ans[1]]=student[0]


ans_friends=0

score=0
for i in range(1,N+1):
    for j in range(1,N+1):
        for student in students:
            if student[0]==arr[i][j]:
                for k in range(4):
                    if arr[i+dx[k]][j+dy[k]] in student:
                        ans_friends+=1
                if ans_friends==1: score+=1
                elif ans_friends==2: score+=10
                elif ans_friends==3: score+=100
                elif ans_friends==4: score+=1000
                ans_friends=0
print(score)

