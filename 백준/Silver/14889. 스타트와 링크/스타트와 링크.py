from itertools import combinations

N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
peoples =  [ i for i in range(N)]
perm = list(combinations(peoples,N//2))
min_gap = 1e8
for start in perm:
    team_check = [False for _ in range(N)]
    team_start = []
    team_link = []
    start_stat = 0
    link_stat = 0
    #10
    for i in start:
        team_check[i] = True
    #20
    for idx in range(N):
        #True면 start
        if team_check[idx]:
            team_start.append(idx)
        else:
            team_link.append(idx)
    # 시너지
    start_len = len(team_start)
    link_len = len(team_link)
    for i in range(start_len-1):
        for j in range(i+1,start_len):
            start_stat += stats[team_start[i]][team_start[j]]
            start_stat += stats[team_start[j]][team_start[i]]
    for i in range(link_len-1):
        for j in range(i+1,link_len):
            link_stat += stats[team_link[i]][team_link[j]]
            link_stat += stats[team_link[j]][team_link[i]]
    min_gap = min(abs(start_stat-link_stat), min_gap)
print(min_gap)
    
