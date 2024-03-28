import sys
input=sys.stdin.readline
def panda(y, x):

    # 방문했던 dp면 dp값 가져오기
    if dp[y][x] != 0:
        return dp[y][x]

    for dy, dx in [[0,-1],[1,0],[-1,0],[0,1]]:
        ey = y + dy
        ex = x + dx

        if 0 <= ey < n and 0 <= ex < n:
            if graph[y][x] < graph[ey][ex]:
                dp[y][x] = max(dp[y][x], panda(ey, ex) + 1)

    return dp[y][x]    # 이동 불가하면 0

n = int(input())    # 그래프의 크기

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]


for y in range(n):
    for x in range(n):
        panda(y, x)

print(max(map(max,dp)) + 1)