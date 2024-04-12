bingo=[list(map(int, input().split())) for i in range(5)]
nums=[list(map(int, input().split())) for i in range(5)]
checks=[[False for _ in range(5)] for _ in range(5)]
def find_bingo():
    bingo_count=0
    
    for i in range(5):
        flag=False
        #i줄이 모두 True면 빙고
        for j in range(5):
            if checks[i][j]==False:
                flag=True
        if flag==False: bingo_count+=1
        
    for i in range(5):
        flag=False
        #i줄이 모두 True면 빙고
        for j in range(5):
            if checks[j][i]==False:
                flag=True
        if flag==False: bingo_count+=1
    
    if checks[0][0]==True and checks[1][1]==True and checks[2][2]==True and checks[3][3]==True and checks[4][4]==True:
        bingo_count+=1
    if checks[0][4]==True and checks[1][3]==True and checks[2][2]==True and checks[3][1]==True and checks[4][0]==True:
        bingo_count+=1
        
    
    
    if bingo_count>=3:
        return True
    else:
        return False
    
    return
def check(number):
    for i in range(5):
        for j in range(5):
            if bingo[i][j]==number:
                return i,j

count=0

going=True
for i in range(5):
    for j in range(5):
        x,y=check(nums[i][j])
        checks[x][y]=True
        count+=1
        if find_bingo():
            going=False
            print(count)
            break
    if going==False:
        break