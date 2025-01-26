def solution(triangle):
    dp=[]
    tri_len=len(triangle)
    for i in range(tri_len):
        temp_list = [0 for _ in range(i+1)]
        dp.append(temp_list.copy())
    dp[0][0]=triangle[0][0]
    for i in range(1,tri_len):
        for j in range(i+1):
            if j==0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j==i:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(triangle[i][j]+dp[i-1][j-1],triangle[i][j]+dp[i-1][j])
    
            
    
    answer = 0
    for i in dp:
        answer = max(answer,max(i))
    return answer