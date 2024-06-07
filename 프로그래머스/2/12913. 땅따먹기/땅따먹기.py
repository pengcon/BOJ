def solution(land):
    answer = 0
    # N행
    N = len(land)
    # dp 생성
    dp = [[0 for _ in range(4)] for _ in range(N)]
    # 1행은 자기의 값을 dp로
    for i in range(4):
        dp[0][i] = land[0][i]
    # 2행부터 N-1행까지
    for i in range(1,N):
        # 0열부터 4열까지
        for j in range(4):
            # i+1행 j+1열의 DP는 이전행에서 같은 열이 아닌 최대값과 land[i][j]의 값을 더해줌
            dp[i][j] = max(dp[i-1][0:j]+dp[i-1][j+1:5]) + land[i][j]
    #최댓값은 DP 마지막 행의 최댓값
    answer = max(dp[N-1])

    return answer