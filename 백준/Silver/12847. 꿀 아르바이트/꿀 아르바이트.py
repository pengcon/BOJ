n,m = map(int,input().split())
lst = list(map(int,input().split()))

start =0 
end = m
s = sum(lst[0:end])
ans = s
for i in range(n-m):
    s -= lst[i]
    s += lst[i+m]
    ans = max(ans, s)
print(ans)