# 14:20
from collections import deque
import sys
sys.setrecursionlimit(10**6)
import sys
input=sys.stdin.readline
N=int(input())
node=[[] for i in range(N+1)]
ans=0

mid_visited=[]
def mid(idx):
    if node[idx][0]!= -1:
        mid(node[idx][0])
    mid_visited.append(idx)
    if node[idx][1]!= -1:
        mid(node[idx][1])


def semi_mid(idx):
    global ans
    stop=False
    
  

    if node[idx][0]!= -1:
        ans+=1
        stop=semi_mid(node[idx][0])
        if stop:
            return True
        else:
            ans+=1

    if node[idx][1]!= -1:
        ans+=1
        stop=semi_mid(node[idx][1])
        if stop:
            return True
        else:
            ans+=1
    if idx==last:
        return True
    return False

    
 
for _ in range(N):
    temp_node,temp_left,temp_right=map(int,input().split())
    node[temp_node]=[temp_left,temp_right]

mid(1)
last=mid_visited[-1]

semi_mid(1)
print(ans)    
