N, M, K = map(int, input().split())
# 파이어볼의 리스트
arr = [[[] for _ in range(N)] for _ in range(N)] 
# 파이어볼 위치 리스트
fireballs=[]
# 0~8
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]
even_direction = [0,2,4,6]
odd_direction = [1,3,5,7]
ans = 0
#처음 파이어볼 입력
for _ in range(M):
    # 행,열,질량,속력,방향
    r, c, m, s, d = list(map(int, input().split()))
    arr[r-1][c-1].append([m,s,d])
    fireballs.append([r-1,c-1])
#이동 횟수만큼
for _ in range(K):
    moved_fireball=[]
    # 파이어볼 이동
    for x,y in fireballs:
        m,s,d = arr[x][y].pop()
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        moved_fireball.append([nx, ny, m, s, d])
    fireballs=[]
    #이동한 파이어볼 arr에 넣어줌
    for mx, my, m, s, d in moved_fireball:
        arr[mx][my].append([m,s,d])
    # 2개 이상이면 파이어볼 합치기
    for i in range(N):
        for j in range(N):
            # 한칸에 하나 있으면
            if len(arr[i][j]) == 1:
                fireballs.append([i,j])
            # 한 칸에 파이어볼 2개 이상 있으면
            if len(arr[i][j])>=2:
                sum_len=len(arr[i][j])
                sum_m = 0
                sum_s = 0
                even = False
                odd = False
                for _ in range(len(arr[i][j])):
                    m, s, d = arr[i][j].pop()
                    sum_m += m
                    sum_s += s
                    # 방향 홀짝 확인
                    if d%2 ==0:
                        even = True
                    else:
                        odd = True
                
                div_m = sum_m // 5
                div_s = sum_s // sum_len
                # 질량이 0 이면 걍 소멸,
                # 0 이상이면 추가
                if div_m>0:
                    if even == False or odd == False:
                        for d in even_direction:
                            arr[i][j].append([div_m,div_s,d])
                            fireballs.append([i,j])
                    else:
                        for d in odd_direction:
                            arr[i][j].append([div_m,div_s,d])    
                            fireballs.append([i,j])  
       
for i in range(N):
    for j in range(N):
        for k in arr[i][j]:
            ans += k[0]
print(ans)