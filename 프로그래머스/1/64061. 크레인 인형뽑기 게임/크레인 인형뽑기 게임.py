def solution(board, moves):
    answer = 0
    basket=[]
    N = len(board)
    for move in moves:
        for i in range(N):
            if board[i][move-1]!=0:
                basket.append(board[i][move-1])
                board[i][move-1]=0
                break
        if len(basket)>1 and basket[-1]==basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
    return answer