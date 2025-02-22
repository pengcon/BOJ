def solution(sizes):
    garo = 0
    sero = 0
    for card in sizes:
        if max(garo,card[0])*max(sero,card[1]) > max(garo,card[1])*max(sero,card[0]):
            garo = max(garo,card[1])
            sero = max(sero,card[0])
        else:
            garo = max(garo,card[0])
            sero = max(sero,card[1])
    answer = garo*sero
    return answer