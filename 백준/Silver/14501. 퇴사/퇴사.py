N=int(input())
dp= [-1 for i in range(N+1)]
t=[0]
p=[0]
for i in range(N):
    temp_t,temp_p=map(int,input().split())
    t.append(temp_t)
    p.append(temp_p)

def recur(idx):
    if idx==N+1:
        return 0 
    if idx>N+1:
        return -99999999
    if dp[idx] != -1:
        return dp[idx]
    
    dp[idx] = max(recur(idx+t[idx]) +p[idx], recur(idx+1))
    
    return dp[idx]
# print(t)
# print(p)
ans=recur(1)
print(ans)