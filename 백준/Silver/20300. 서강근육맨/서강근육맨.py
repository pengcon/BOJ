from collections import deque
n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
n_deque=deque(n_list)
# print(len(n_deque))

M=0
if len(n_deque)%2 != 0:
    M=n_deque.pop()
else:
    temp_M=n_deque.pop()+n_deque.popleft()
    M=temp_M 

while len(n_deque)!= 0:
    temp_M=n_deque.pop()+n_deque.popleft()
    if M<temp_M:
        M=temp_M
print(M)