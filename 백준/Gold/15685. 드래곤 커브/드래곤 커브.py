N=int(input())
curve=[]
#우 상 좌 하 
dx=[1,0,-1,0]
dy=[0,-1,0,1]

new_dx=[0,1,0,-1]
new_dy=[1,0,-1,0]
ans=[]
temp=set()
ans_count=0
for _ in range(N):
    x,y,d,g=map(int,input().split())
    curve.append([x,y,d,g])

for x,y,d,g in curve:
    # 시작 좌표
    direction=[[x,y]]
    # 0단계 좌표
    direction.append([x+dx[d],y+dy[d]])
    # 단계 동안 반복
    for _ in range(g):
        new_x=direction[-1][0]
        new_y=direction[-1][1]
        for i in range(len(direction)-1,0,-1):
            #오른쪽
            if direction[i-1][0]-direction[i][0]>0:
                new_x=new_x+new_dx[0]
                new_y=new_y+new_dy[0]
            #위쪽
            elif direction[i-1][1]-direction[i][1]<0:
                new_x=new_x+new_dx[1]
                new_y=new_y+new_dy[1]
            #왼쪽
            elif direction[i-1][0]-direction[i][0]<0:
                new_x=new_x+new_dx[2]
                new_y=new_y+new_dy[2]
            #아래
            elif direction[i-1][1]-direction[i][1]>0:
                new_x=new_x+new_dx[3]
                new_y=new_y+new_dy[3]

            direction.append([new_x,new_y])
    for ans_x,ans_y in direction:
        if (ans_x,ans_y) not in temp:
            ans.append([ans_x,ans_y])
            temp.add((ans_x,ans_y))

ans.sort()
for i,j in ans:
    if (i+1,j) in temp and (i,j+1) in temp and (i+1,j+1) in temp:
        ans_count += 1 

print(ans_count)