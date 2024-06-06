N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
#초기 비구름 생성
forg = [[N-1,0], [N-2,0], [N-1,1], [N-2,1]]
#1~8 (0번은 더미값)
#대각선은 2,4,6,8
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
ans = 0
#이동 반복
for _ in range(M):
    d, s = map(int, input().split())
    # 4번에서 이용할 물이 증가한 칸
    meet_forg=set()
    # 1. 구름 이동 후
    for r,c in forg:
        nx = (r + dx[d] * s) % N 
        ny = (c + dy[d] * s) % N
        # 2. 물 +1
        arr[nx][ny] += 1
        # 4번에 사용할 바뀐 구름 칸
        meet_forg.add((nx,ny))
        # 5번에 사용할 소멸할 구름 칸 

    # 3. 구름 소멸
    forg = []
    # 4. 증가칸 대각선 물 체크
    for x,y in meet_forg:
        for i in range(2,9,2):
            mx=x+dx[i]
            my=y+dy[i]
            #경계를 못 넘음
            if 0<=mx<N and 0<=my<N and arr[mx][my]>0:
                arr[x][y] += 1
    # 5.
    for j in range(N):
        for k in range(N):
            if arr[j][k]>=2 and (j,k) not in meet_forg:
                arr[j][k] -= 2
                forg.append([j,k])
for i in arr:
    ans += sum(i)
print(ans)