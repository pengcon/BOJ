

N=int(input())
min_num=1_000_000_000
ingre = [list(map(int,input().split())) for _ in range(N)]
def recur (idx,sin,sseun):
    global min_num
    if idx==N :
        if sin!=1 and sseun!=0:
            if min_num>abs(sin-sseun):
                min_num=abs(sin-sseun)
        return 
    recur(idx+1,sin,sseun)
    recur(idx+1,sin*ingre[idx][0],sseun+ingre[idx][1])
recur(0,1,0)
# print(ingre)
print(min_num)