import heapq
import sys
input = sys.stdin.readline
n = int(input())
hq = []
size = 0
for i in range(n):
    num = int(input())
    if num == 0:
        if size>0:
            print(-heapq.heappop(hq))
            size -=1
        else:
            print(0)
    else:
        heapq.heappush(hq,-num)
        size+=1