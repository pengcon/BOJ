import heapq
import sys
input=sys.stdin.readline
n=int(input())
q=[]

for i in range(n):
    temp=int(input())
    if temp != 0 :
        heapq.heappush(q,(abs(temp),temp))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])