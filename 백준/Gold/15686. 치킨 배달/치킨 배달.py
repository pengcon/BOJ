N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
bbq=[]
house=[]
ans=1e8
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i,j])
        if arr[i][j] == 2:
            bbq.append([i,j])

alive_bbq=[]

def find_chicken_distance(alive_bbq):
    dist=0
    for house_x,house_y in house:
        house_dist=1e9
        for bbq_x,bbq_y in alive_bbq:
            chick_dist = abs(house_x - bbq_x) + abs(house_y - bbq_y)
            house_dist = min(house_dist, chick_dist)
        dist += house_dist
    return dist


def backtracking(start):
    global ans
    if len(alive_bbq)==M:
        ans=min(ans,find_chicken_distance(alive_bbq))
        return
    for i in range(start,len(bbq)):
        alive_bbq.append(bbq[i])
        backtracking(i+1)
        alive_bbq.pop()

backtracking(0)
print(ans)