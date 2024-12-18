# 5547 일루미네이션
from collections import deque

m, n = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

answer = 0
visited = [[False] * (m+2) for _ in range(n+2)]

# y = 짝수
dx = [0, -1, -1, -1, 0, 1]
dy = [-1, -1, 0, 1, 1, 0]
# y = 홀수
cx = [0, -1, 0, 1, 1, 1]
cy = [-1, 0, 1, 1, 0, -1]

# 외곽 부분 0으로 마스킹
graph = [[0] * (m+2) for _ in range(n+2)]
for i in range(n):
    for j in range(m):
        graph[i+1][j+1] = array[i][j]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True
    count = 0
    while queue:
        y, x = queue.popleft()
        if y % 2 == 0: # 짝수일때
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= m+2 or ny >= n+2:
                    continue
                # 0과 1이 연결되어 있으면 체크
                if graph[ny][nx] == 1:
                    count += 1
                elif graph[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True

        else:
            for i in range(6):
                nx = x + cx[i]
                ny = y + cy[i]
                if nx < 0 or ny < 0 or nx >= m+2 or ny >= n+2:
                    continue

                if graph[ny][nx] == 1:
                    count += 1
                elif graph[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
    return count

print(bfs(0,0))