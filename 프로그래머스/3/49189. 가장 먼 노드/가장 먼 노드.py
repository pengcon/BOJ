from collections import deque
from collections import defaultdict
def solution(n, edge):
    dict=defaultdict(list)
    n_list = [0 for  _ in range(n+1)]
    for i in edge:
        dict[i[0]].append(i[1])
        dict[i[1]].append(i[0])
    visited = set()
    q = deque()
    q.append((1,0))
    visited.add(1)
    while q:
        num,g = q.popleft()
        n_list[num] = g
        for i in dict[num]:
            if i not in visited:
                q.append((i,g+1))
                visited.add(i)
    max_num = max(n_list)
    answer = 0 
    for i in n_list:
        if max_num==i:
            answer += 1
        
    return answer