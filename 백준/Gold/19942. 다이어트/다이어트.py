import sys
input=sys.stdin.readline
N=int(input())
min_a,min_b,min_c,min_d=map(int,input().split())
ingre=[list(map(int,input().split()))for i in range(N)]
money=999999999999
visited=[]
visit=[]
def back(idx,a,b,c,d,e,visited):
    # print(idx)
    global money
    global visit
    if idx==N:
        if a>=min_a and b>=min_b and c>=min_c and d>=min_d:
            if money>e:
                money=e
                visit=[]
                visit.append(visited.copy())
            if money==e:
                visit.append(visited.copy())
        return
    visited.append(idx+1)
    back(idx+1,a+ingre[idx][0],b+ingre[idx][1],c+ingre[idx][2],d+ingre[idx][3],e+ingre[idx][4],visited)
    visited.pop()
    back(idx+1,a,b,c,d,e,visited)
    return
back(0,0,0,0,0,0,visited)
if money==999999999999:
    print(-1)
else:
    print(money)
    # print(visit)
    visit.sort()
    print(*visit[0])