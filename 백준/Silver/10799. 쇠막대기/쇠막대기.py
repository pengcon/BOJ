dq =[]
st = input()

ans = 0
for i in range(len(st)):
    if st[i]=='(':
        dq.append(st[i])
    elif st[i]==')':
        if st[i-1]=='(':
            dq.pop()
            ans += len(dq)
        elif st[i-1]==')':
            dq.pop()
            ans += 1
print(ans)
        