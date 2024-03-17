import sys
input=sys.stdin.readline
n=int(input())
x_list=[]
y_list=[]
find_list=[]
#x와 y값을 넣어줌
for i in range(n):
    x,y=map(int,input().split())
    x_list.append(x)
    y_list.append(y)
#탐색할 범위를 정해줌
for i in x_list:
    for j in y_list:
        if [i,j] not in find_list:
            find_list.append([i,j])
distance_list=[[] for i in range(len(find_list))]            

#탐색하는 범위마다 좌표와의 거리를 정해주고 크기 순 정렬
for i in range(len(find_list)):
    for j in range(n):
        dis=abs(find_list[i][0]-x_list[j])+abs(find_list[i][1]-y_list[j])
        distance_list[i].append(dis)
    distance_list[i].sort()
# print(distance_list)
#최소 거리를 찾아줌
for i in range(n):
    min=300_000_000
    for j in distance_list:
        temp=sum(j[0:i+1])
        if temp<min:
            min=temp
    print(min,end=' ')
