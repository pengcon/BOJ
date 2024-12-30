def queen(k):
    global n, cnt
    
    if k == n :
        cnt += 1
        return

    for i in range(n):
        if not used_column[i] and not used_dia1[k+i] and not used_dia2[k-i+n-1]:
            used_column[i] = True
            used_dia1[k+i] = True
            used_dia2[k-i+n-1] = True
            queen(k+1)
            used_column[i] = False
            used_dia1[k+i] = False
            used_dia2[k-i+n-1] = False


n = int(input())
maps = [[0]*n for _ in range(n)]

used_column = [False]*n
used_dia1 = [False]*(2*(n-1)+1)
used_dia2 = [False]*(2*(n-1)+1)

cnt = 0

## output
queen(0)
print(cnt)