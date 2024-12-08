import heapq

n = int(input())
a=[]
for i in range(n):
    for b in list(map(int,input().split())):
        heapq.heappush(a,b)
        if len(a)>n:
            heapq.heappop(a)


print(heapq.heappop(a))