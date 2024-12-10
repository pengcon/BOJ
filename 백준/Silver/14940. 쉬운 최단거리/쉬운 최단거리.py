from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1] * m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            queue.append((i, j))
            ans[i][j] = 0
        elif arr[i][j] == 0:
            ans[i][j] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and ans[nx][ny] == -1 and arr[nx][ny] != 0:
            ans[nx][ny] = ans[x][y] + 1
            queue.append((nx, ny))

for row in ans:
    print(*row)