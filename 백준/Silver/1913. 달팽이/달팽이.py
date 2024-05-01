import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
lists=[[0 for _ in range(N)] for _ in range(N)]
idx=N*N
temp=N

def down(temp):
   global idx
   #x시작점을 1씩올림 = N-temp
   #x도착점을 1씩 줄임 = temp
   #y를 1 씩 늘림 = [][N-temp]
   for i in range(N-temp,temp):
        lists[i][N-temp]=idx
        idx-=1
    
   #y시작점을 1씩올림 = N-temp
   #y도착점을 1씩 줄임 = temp
   #x를 1씩 줄임[temp-1][]
def right(temp):
   global idx
   for i in range(N-temp+1,temp):
        lists[temp-1][i]=idx
        idx-=1 

   #x시작점을 1씩줄임 = temp-2
   #x도착점을 1씩 올림 = N-temp-1
   #y를 1씩 줄임= [][temp-1]
def up(temp):
   global idx
   for i in range(temp-2,N-temp-1,-1):
        lists[i][temp-1]=idx
        idx-=1 
    #y시작점을 1씩 줄임 = temp-2
    #y도착점을 1씩 올림 = N-temp
    #x를 1씩 늘림 [N-temp][]
def left(temp):
    global idx
    for i in range(temp-2,N-temp,-1):
        lists[N-temp][i]=idx
        idx-=1
    return temp-1
while (idx>0):
    down(temp)
    right(temp)
    up(temp)
    temp=left(temp)
for i in lists:
    print(*i)
for j in range(N):
    for k in range(N):
        if lists[j][k]==M:
            print(j+1,k+1)