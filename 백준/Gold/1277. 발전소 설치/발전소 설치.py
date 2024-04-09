import heapq
import math
#발전소 수, 연결되어있는 전선 수 
N,W =map(int,input().split())
#거리 제한
M=float(input())


# 발전소 좌표
loc=[[-1,-1]]

for i in range(N):
    x,y=map(int,input().split())
    loc.append([x,y])
# 연결 정보
links = [[] for _ in range(N+1)]
# 최단 거리 
dist = [1e9 for _ in range(N+1)]
#1번 발전소는 거리가 0
dist[1] = 0


#연결되어있는 전선의 리스트들
# zero_list=dict()
# for i in range(N+1):
#     zero_list[i]=-1




# 사전에 연결되어있는 발전소는 연결거리와 최단거리가 0
# A에서 B로가는 비용이 C이다
for _ in range(W):
    A,B = map(int,input().split())
    links[A].append([B,0])
    links[B].append([A,0])
    # dist[B]=0
    # zero_list[A]=B
    # zero_list[B]=A
#1000*1000
for i in range(1,N+1):
    for j in range(1,N+1):
        if i!=j:
            # if zero_list[i]!=j:
            _dist=math.sqrt((loc[i][0] - loc[j][0])**2 + (loc[i][1]-loc[j][1])**2)
            if _dist<=M:
                links[i].append([j,_dist])


# #bfs
q = []
# #번호,거리
heapq.heappush(q,[1,0])




while q:
    #우선순위 큐로 거리보고 정렬
 
    node,weight =heapq.heappop(q)
    for nxt,weight in links[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt]=dist[node] + weight
            heapq.heappush(q, [nxt,dist[nxt]])   

# print(dist)    
print(int(dist[N]*1000))