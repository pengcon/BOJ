N=int(input())
#상하좌우
lists=[[" "for _ in range(4*(N-1)+1)] for _ in range(4*(N-1)+1) ]
dx= [-1,1,0,0]
dy= [0,0,-1,1]
curx=0
cury=0
temp=4*(N-1)+1
def down(temp):
    global curx,cury
 
    for i in range(temp-1):
        # print(curx)
        curx=curx+dx[1]
        cury=cury+dy[1]
        lists[curx][cury]="*"
def right(temp):
    global curx,cury
    for i in range(temp-1):
        curx=curx+dx[3]
        cury=cury+dy[3]
        lists[curx][cury]="*"

def up(temp):
    global curx,cury
    for i in range(temp-1):
        curx=curx+dx[0]
        cury=cury+dy[0]
        lists[curx][cury]="*"
def left(temp):
    global curx,cury
    for i in range(temp-1):
        curx=curx+dx[2]
        cury=cury+dy[2]
        lists[curx][cury]="*"
while temp>0:
    if temp>1:
        down(temp)
        right(temp)
        up(temp)
        left(temp)
        temp-=4
        curx+=2
        cury+=2
    elif temp==1:
        lists[curx][cury]="*"
        temp=0
for i in lists:
    for j in i:
        print(j,end='')
    print()
 
    